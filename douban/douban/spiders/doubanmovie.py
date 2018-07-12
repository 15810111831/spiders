# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    start_urls = (
        url + str(offset),
    )


    def parse(self, response):
        item = DoubanItem()
        infos = response.xpath('//div[@class="info"]')
        for info in infos:
            name = info.xpath('.//span[@class="title"][1]/text()').extract()[0]
            body = info.xpath('.//div[@class="bd"]/p[1]/text()').extract()[0]
            star = info.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = info.xpath('.//div[@class="bd"]//p[@class="quote"]/span[@class="inq"]/text()').extract()

            item['name'] = name
            item['body'] = body
            item['star'] = star

            if len(quote) == 0:
                item['quote'] = ""
            else:
                item['quote'] = quote[0]

            yield item

        if self.offset < 250:
            self.offset +=25

        yield scrapy.Request(self.url + str(self.offset), callback= self.parse)




