# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TpositionSpider(scrapy.Spider):
    name = "tPosition"
    allowed_domains = ["tencent.com"]
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentItem()
            #通过extract将选择器对象转换为unicode字符串
            positionName = each.xpath('./td[1]/a/text()').extract()[0]
            positionLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionType = each.xpath('./td[2]/text()').extract()
            people = each.xpath('./td[3]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]
            pubTime = each.xpath('./td[5]/text()').extract()[0]


            item['name'] = positionName
            item['positionLink'] = positionLink
            item['positionType'] = positionType
            item['peopleNum'] = people
            item['workLocation'] = workLocation
            item['pubTime'] = pubTime

            yield item

        if self.offset < 1680:
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)


