# -*- coding: utf-8 -*-
# 产生这个文件的命令为项目根目录下scrapy genspider jobbole blog.jobbole.com
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        pass
