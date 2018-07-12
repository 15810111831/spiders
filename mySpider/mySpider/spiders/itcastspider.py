#coding:utf-8
import scrapy
from mySpider.items import MyspiderItem

#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    #允许爬虫作用的范围
    allowd_domains = ['http://www.itcast.cn/']
    #设置爬取的起始地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac',
                  'http://www.itcast.cn/channel/teacher.shtml#acloud',
                  'http://www.itcast.cn/channel/teacher.shtml#ads',
                  'http://www.itcast.cn/channel/teacher.shtml#ago',
                  'http://www.itcast.cn/channel/teacher.shtml#ajavaee',
                  'http://www.itcast.cn/channel/teacher.shtml#aLinux',
                  'http://www.itcast.cn/channel/teacher.shtml#amovies',
                  'http://www.itcast.cn/channel/teacher.shtml#anetmarket',
                  'http://www.itcast.cn/channel/teacher.shtml#aphp',
                  'http://www.itcast.cn/channel/teacher.shtml#apm',
                  'http://www.itcast.cn/channel/teacher.shtml#apython',
                  'http://www.itcast.cn/channel/teacher.shtml#astack',
                  'http://www.itcast.cn/channel/teacher.shtml#atest',
                  'http://www.itcast.cn/channel/teacher.shtml#aui',
                  'http://www.itcast.cn/channel/teacher.shtml#auijp',
                  'http://www.itcast.cn/channel/teacher.shtml#aweb',
                  'http://www.itcast.cn/channel/teacher.shtml#awlw']

    def parse(self, response):

        #选出所有老师信息列表
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 所有老师信息的集合
        # teacherItem = []

        for teacher in teacher_list:
            item = MyspiderItem()
            name = teacher.xpath('./h3/text()').extract()
            title = teacher.xpath('./h4/text()').extract()
            info = teacher.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            #交给pipelines 处理
            yield item

            # teacherItem.append(item)

        # return teacherItem
