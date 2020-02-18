# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import json

# class BotPipeline(object):
#     def __init__(self):
#         self.file = open('jokes.txt','w',encoding='utf-8')

#     def open_spider(self, spider):
#         print('爬虫开始')

#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.file.write(item_json+'\n')
#         return item

#     def close_spider(self,spider):
#         self.file.close()
#         print('over')

from scrapy.exporters import JsonLinesItemExporter

class BotPipeline(object):
    def __init__(self):
        self.file = open('jokes.txt','wb')
        self.exporter = JsonLinesItemExporter(self.file,ensure_ascii=False)

    def open_spider(self, spider):
        print('start')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.file.close()
        print('over')
