# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapyDemoPipeline(object):
#     def process_item(self, item, spider):
#         return item
import urllib2


class DouYuPipline(object):

    def __init__(self):
        self.csv_file = open("douyu.csv", "w")

    def process_item(self, item, spider):
        text = item["title"] + "," + str(item["hot"]) + "," + item["img_url"] + "\n"
        # with open("img/" + item["title"] + "_" + str(item["hot"]) + ".jpg", "wb") as f:
        #     f.write(urllib2.urlopen(item["img_url"]).read())
        self.csv_file.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.csv_file.close()
