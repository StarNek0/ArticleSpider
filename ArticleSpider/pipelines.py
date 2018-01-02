# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 数据存储相关


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

import codecs
import json
class JsonWithEncodingPipeline(object):
    # a)自己导出到Json文件
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")  # codecs能够更好的读取文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + 'n'  # ensure_ascii=False 否则中文和其他编码文件报错
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        spider.file.close()

class JsonExporterPipeline(object):
    # b)调用Scrapy本身提供的json export导出到json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        # 调用JsonItemExporter初始化该参数
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

import MySQLdb
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'klxsxzsdf1', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        insert_sql = """
            INSERT INTO jobbole_article(title, url, create_date, fav_nums) 
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['url'], item['create_date'], item['fav_nums']))
        self.conn.commit()


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for status, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        return item