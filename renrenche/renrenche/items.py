# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrencheItem(scrapy.Item):
    name = scrapy.Field()

    title = scrapy.Field()
    city = scrapy.Field()
    small = scrapy.Field()
    summary = scrapy.Field()
    travel = scrapy.Field()
    price = scrapy.Field()
