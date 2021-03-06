# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PttItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    push = scrapy.Field()
    url = scrapy.Field()
    last_page = scrapy.Field()
    pass

class AppleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    view = scrapy.Field()
    pass


