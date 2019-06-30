# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    cname = scrapy.Field()
    title = scrapy.Field()
    requires = scrapy.Field()
    input_time = scrapy.Field()
    lure = scrapy.Field()
    repr = scrapy.Field()
    addr = scrapy.Field()
    pass
