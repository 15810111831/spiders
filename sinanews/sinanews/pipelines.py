# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class SinanewsPipeline(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017
        self.client = pymongo.MongoClient(host = self.host, port = self.port)
        self.db = self.client['sina']
        self.sheet = self.db['news']


    def process_item(self, item, spider):
        self.sheet.insert(dict(item))
        if item['head']:
            filename = item['head'] + '.txt'
        else:
            filename = item['sonUrl'][-11:-6] + '.txt'

        with open(item['subFileName'] +'/'+filename, 'wb') as f:
            f.write(item['content'].encode('utf-8'))

        return item
