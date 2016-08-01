# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field

class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["huajiao.com"]
    start_urls = []
    start_urls.append('http://www.huajiao.com/category/2')
    def __init__(self, *a, **kw):
        for i in range(1, 200):
            self.start_urls.append('http://www.huajiao.com/category/2?pageno=%d'%i)

    def parse(self, response):
        sites=response.selector.xpath('//div[@id="doc-bd"]//div[@class="container clearfix"]//div[@class="main"]//div[@class="g-box feed-list cat-1"]//div[@class="box-bd"]//ul//li')
        print "len",len(sites)
	for site in sites:
            document_extract = site.xpath('//p//span[@class="username"]//text()').extract()
            print document_extract
            print "\n"
        pass
