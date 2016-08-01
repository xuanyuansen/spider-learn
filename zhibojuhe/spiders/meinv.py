# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field

class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["huajiao.com"]
    start_urls = []
    start_urls.append('http://www.huajiao.com/category/2')
    def __init__(self, *a, **kw):
        for i in range(2, 200):
            self.start_urls.append('http://www.huajiao.com/category/2?pageno=%d'%i)

    def parse(self, response):
        sites=response.selector.xpath('//div[@id="doc-bd"]//div[@class="container clearfix"]//div[@class="main"]//div[@class="g-box feed-list cat-1"]//div[@class="box-bd"]//ul//a')
        print "len",len(sites)
	for site in [sites[1]]:
            print site
            document_extract = site.xpath('//p//span[@class="username"]//text()').extract()
            document_extract2 = site.xpath('//div[@class="comment-inner"]//text()').extract()
            for ele in document_extract:
                print ele
           
            for ele in document_extract2:
                print ele
            print "\n"
        pass
