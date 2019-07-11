# !/usr/bin/python
# -*- coding: UTF-8 -*-

# !/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DouYuSpider(CrawlSpider):
    name = "douyuCrawl"
    # allowed_domains = ["www.douyu.com"]
    url = "https://www.douyu.com/directory/all"
    start_urls = [url]

    links = LinkExtractor(allow="https")

    rules = [
        Rule(links, callback="link_handle")
    ]

    def link_handle(self, response):
        print response.body
