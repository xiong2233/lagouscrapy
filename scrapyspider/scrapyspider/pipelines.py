# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ScrapyspiderMongoDBPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            MONGO_HOST,MONGO_PORT
        )
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)
        return item

    def close_spider(self, spider):
        print('执行了close_spider函数')

