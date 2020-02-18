# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from bot.items import BotItem
import re

class JokeSpider(scrapy.Spider):
    name = 'joke'
    allowed_domains = ['m.qiushi.92game.net']
    start_urls = ['http://m.qiushi.92game.net/']
    base_url = 'http://m.qiushi.92game.net/'

    def parse(self, response):
        jokes = response.xpath('//div[@class="qiushi"]').getall()
        for joke in jokes:
            joke = ''.join(joke).strip()
            item = BotItem(content=joke)
            yield item
        
        page_url = response.xpath('//div[@class="pagebar footer"]/a[last()]/@href').get()
        page_text = response.xpath('//div[@class="pagebar footer"]/a[last()]/text()').get()
        print(page_url)
        next_url=self.base_url+page_url
        if page_text == '下一页':
            print(next_url)
            # yield scrapy.Request(next_url,callback=self.parse)
        else:
            return





