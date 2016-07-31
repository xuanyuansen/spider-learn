# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ZhibojuheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = Field()
    image_names = Field()
    image_paths = Field()
    image = Field()
    user_name  = Field()
    useful_info_id  = Field()
    useful_info_desc  = Field()
    useful_info_follow  = Field()
    useful_info_fans  = Field()
    useful_info_like  = Field()
    useful_info_exp  = Field()
    pass
