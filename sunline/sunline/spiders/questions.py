# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunlineItem

class QuestionsSpider(CrawlSpider):
    name = 'questions'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    pageLinks = LinkExtractor(allow = r'/questionType?type=4&page=\d+')

    questionLinks = LinkExtractor(allow = r'/question/\d+/\d+.shtml')

    rules = (
        Rule(pageLinks, follow=True, callback = 'parseUrl'),
        # Rule(questionLinks, callback = 'parse_question', follow = False),
    )

    def parse_question(self, response):
        item = SunlineItem()

        item['url'] = response.url
        item['title'] = response.xpath('//strong[@class="tgray14"]').extract()[0].split(' ')[:-1]
        item['num'] = response.xpath('//strong[@class="tgray14"]').extract()[0].split(' ')[-1].split(":")[-1]
        item['content'] = response.xpath('//div[@class="c1 text14_2"]').extract()[0]

        yield item

    def parseUrl(self, response):
        print response.url