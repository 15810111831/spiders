# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class MovieInfoPipeline(object):
    def __init__(self):
        host = settings['MONGO_HOSTG']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        sheetName = settings['MONGO_DOCNAME']
        client = pymongo.MongoClient(host = host, port = port)
        mydb = client[dbname]
        self.mysheet = mydb[sheetName]

    def process_item(self, item, spider):
        data = dict(item)
        self.mysheet.insert(data)

        return item

    def close_spider(self):
        print '数据存储完成'

