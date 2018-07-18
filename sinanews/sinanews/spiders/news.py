# -*- coding: utf-8 -*-
import scrapy
import os
from sinanews.items import SinanewsItem
from scrapy_redis.spiders import RedisSpider

class NewsSpider(RedisSpider):
    name = "news"
    allowed_domains = ["sina.com.cn"]
    # start_urls = (
    #     'http://news.sina.com.cn/guide/',
    # )
    redis_key = 'newsspider:start_urls'

    # def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        # domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))
        # super(NewsSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        items = []
        #所有大标题的url和titile
        parentUrls = response.xpath('//div[@id=\"tab01\"]/div/h3/a/@href').extract()
        parentTitles = response.xpath('//div[@id=\"tab01\"]/div/h3/a/text()').extract()
        #所有小标题的url和title
        subUrls = response.xpath('//div[@id=\"tab01\"]/div/ul/li/a/@href').extract()
        subTitles = response.xpath('//div[@id=\"tab01\"]/div/ul/li/a/text()').extract()

        for i in range(0,len(parentUrls)):
            #根据大标题创建文件夹
            parentName = './Data/' + parentTitles[i]
            if not os.path.exists(parentName):
                os.makedirs(parentName)

            for j in range(0,len(subUrls)):
                item = SinanewsItem()
                item['parentUrl'] = parentUrls[i]
                item['parentTitle'] = parentTitles[i]

                if subUrls[j].startswith(item['parentUrl']):
                    #根据小类创建文件夹
                    subName = parentName + '/' +subTitles[j]
                    if not os.path.exists(subName):
                        os.makedirs(subName)

                    item['subTitle'] = subTitles[j]
                    item['subUrl'] = subUrls[j]
                    item['subFileName'] = subName
                    items.append(item)

        for item in items:
            yield scrapy.Request(url = item['subUrl'], meta = {'meta_1':item}, callback = self.parse_second)


    def parse_second(self, response):
        meta_1 = response.meta['meta_1']
        #爬取subUrl中的每一个子链接
        sonUrls = response.xpath('//a/@href').extract()
        items = []
        for i in range(0,len(sonUrls)):
            if sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrl']):
                item = SinanewsItem()
                item['parentUrl'] = meta_1['parentUrl']
                item['parentTitle'] = meta_1['parentTitle']
                item['subUrl'] = meta_1['subUrl']
                item['subTitle'] = meta_1['subTitle']
                item['subFileName'] = meta_1['subFileName']
                item['sonUrl'] = sonUrls[i]

                items.append(item)


        for item in items:
            yield scrapy.Request(url = item['sonUrl'], meta = {'meta_2': item}, callback = self.parse_end)


    def parse_end(self, response):
        item = response.meta['meta_2']

        head = response.xpath('//h1[@class="main-title"]/text()').extract()
        content_list = response.xpath('//div[@id="article"]/p/text() | //div[@id="artibody"]/p/text()').extract()

        content = ''
        for info in content_list:
            content += '\n' + info

        if len(head) > 0:
            item['head'] = head[0]
        else:
            item['head'] = ''
        item['content'] = content

        yield item



