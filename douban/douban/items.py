# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field() #标题
    body = scrapy.Field() #信息
    star = scrapy.Field() #评分
    quote = scrapy.Field() #简介
