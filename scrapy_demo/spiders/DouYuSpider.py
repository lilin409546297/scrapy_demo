# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import scrapy
import time

from scrapy_demo.items import DouYuItem


class DouYuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["www.douyu.com", "rpic.douyucdn.cn"]
    url = "https://www.douyu.com/gapi/rkc/directory/0_0/"
    page = 1
    start_urls = [url + str(page)]

    def parse(self, response):
        data = json.loads(response.text)["data"]["rl"]
        for detail in data:
            douyu_item = DouYuItem()
            douyu_item["title"] = detail["rn"]
            douyu_item["hot"] = detail["ol"]
            douyu_item["img_url"] = detail["rs1"]
            yield scrapy.Request(detail["rs1"], callback=self.img_data_handle)
            yield douyu_item
        self.page += 1
        yield scrapy.Request(self.url + str(self.page), callback=self.parse)

    def img_data_handle(self, response):
        with open("img/" + str(time.time()) + ".jpg", "wb") as f:
            f.write(response.body)