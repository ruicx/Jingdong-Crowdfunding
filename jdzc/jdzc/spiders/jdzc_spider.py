
# -*- coding: utf-8 -*-

'''
name:       jdzc_spider.py
usage:      --
author:     [[
date:       2018-02-18 15:42:19
version:    1.0
Env.:       Python 3.6.4, WIN 10
'''



import scrapy
from jdzc.items import JdzcItem


class DmozSpider(scrapy.spiders.Spider):
    name = "jdzc"
    allowed_domains = ["z.jd.com"]
    # start_urls = [
    #     "https://z.jd.com/bigger/search.html"
    # ]

    def start_requests(self):
        for page in range(1, 100):
            yield scrapy.FormRequest(
                url="https://z.jd.com/bigger/search.html",
                formdata={
                    'page': str(page), 'sort': 'zhtj', 'categoryId': '10'
                    },
                callback=self.parse
            )

    def parse(self, response):
        for sel in response.css('li.info.type_now'):
            item = JdzcItem()
            item['name'] = sel.css('h4.link-tit::text').extract()
            item['progress'] = sel.css('li.fore1 p.p-percent::text').extract()
            item['money'] = sel.css('li.fore2 p.p-percent::text').extract()
            item['time'] = sel.css('li.fore3 p.p-percent::text').extract()
            item['like'] = sel.css('span::text').extract()[0].strip()
            yield item
