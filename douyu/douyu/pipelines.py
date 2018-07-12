# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import  get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ImagePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    IMAGE_STORE = get_project_settings().get('IMAGES_STORE')


    def get_media_requests(self, item, info):
        img_url = item['imgLink']

        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        img_path = [x['path'] for ok,x in results if ok]

        os.rename(self.IMAGE_STORE + img_path[0], self.IMAGE_STORE + item['nickName'] + '.jpg')

        item['imgPath'] = self.IMAGE_STORE + item['nickName']

        return item

