# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .. items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    start_urls = ['http://hr.tencent.com/position.php?&start=']

    pageLinks = LinkExtractor(allow = ('start=\d+'))

    rules = (
        Rule(pageLinks, callback='parsePosition', follow=True),
    )

    def parsePosition(self, response):

        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentItem()

            # 通过extract将选择器对象转换为unicode字符串
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