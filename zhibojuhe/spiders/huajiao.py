# -*- coding: utf-8 -*-
import scrapy
from zhibojuhe.items import ZhibojuheItem
from babel.messages.extract import extract

class HuajiaoSpider(scrapy.Spider):
    name = "huajiao"
    allowed_domains = ["http://www.huajiao.com/"]
    start_urls = []
    def __init__(self, *a, **kw):
        for i in range(31853569, 31953569):
            self.start_urls.append('http://www.huajiao.com/user/%d'%i)

    def parse(self, response):
        sites=response.selector.xpath('//div[@class="container user_index user"]//div[@class="t"]//div[@class="avatar"]/img/@src').extract()
        user_id = response.selector.xpath('//div[@class="container user_index user"]//div[@class="t"]//div[@class="info"]')
        print type(user_id)
        #print user_id
        info_id_about = user_id[0].xpath('//p/text()').extract()
        print "info_id_about"
        useful_info_id  = int(info_id_about[0].split(": ")[1])
        useful_info_desc  = info_id_about[1]
        useful_info_follow  = int(info_id_about[2])
        useful_info_fans  = int(info_id_about[3])
        useful_info_like  = int(info_id_about[4])
        useful_info_exp = 0
        try:
            useful_info_exp = int(info_id_about[5])
        except:
            print "no exp"
            useful_info_follow  = int(info_id_about[1])
            useful_info_fans  = int(info_id_about[2])
            useful_info_like  = int(info_id_about[3])
        
        
        print "useful_info_id",useful_info_id
        print "useful_info_desc",useful_info_desc
        print "useful_info_follow",useful_info_follow
        print "useful_info_fans",useful_info_fans
        print "useful_info_like",useful_info_like
        print "useful_info_exp",useful_info_exp

        user_name = user_id[0].xpath('//h3/text()').extract()
        user_name_extract  = user_name[0].strip().split(" ")[0]
        print "user_name"
        print user_name_extract
        
        print "sites"
        print sites
        
        items = []
        for site in sites:
            item = ZhibojuheItem()
            item['image_urls'] = [site]
            item['image_names'] = site
            item['user_name']  = user_name_extract
            item['useful_info_id'] = useful_info_id
            item['useful_info_desc']  = useful_info_desc
            item['useful_info_follow']  = useful_info_follow
            item['useful_info_fans']  = useful_info_fans
            item['useful_info_like'] = useful_info_like
            item['useful_info_exp'] = useful_info_exp
            items.append(item)
        print "items"
        for item in items:
            print item    
        return items
