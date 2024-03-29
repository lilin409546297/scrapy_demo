# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ScrapyDemoItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class DouYuItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 热度
    hot = scrapy.Field()
    # 图片url
    img_url = scrapy.Field()
