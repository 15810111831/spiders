# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyumeinvSpider(scrapy.Spider):
    name = "douyumeinv"
    allowed_domains = ["capi.douyucdn.cn"]

    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='

    start_urls = [url+str(offset)]
    def parse(self, response):
        data = json.loads(response.text)['data']

        for info in data:
            item = DouyuItem()
            item['nickName'] = info['nickname']
            item['imgLink'] = info['vertical_src']

            yield item

        if self.offset < 300:
            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

