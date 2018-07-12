# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SunlinePipeline(object):
    def __init__(self):
        self.file = open('sunlineQeustion.json', 'wb')

    def process_item(self, item, spider):
        questionJson = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(questionJson.encode('utf-8'))


    def close_spider(self):
        self.file.close()