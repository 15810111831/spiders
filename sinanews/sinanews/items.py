# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    # 大类的标题 和 url
    parentTitle = scrapy.Field()
    parentUrl = scrapy.Field()

    # 小类的标题 和 子url
    subTitle = scrapy.Field()
    subUrl = scrapy.Field()

    # 小类目录存储路径
    subFileName = scrapy.Field()

    # 小类下的子链接
    sonUrl = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()