# -*- coding: utf-8 -*-
# 产生这个文件的命令为项目根目录下scrapy genspider jobbole blog.jobbole.com
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/111865/']

    def parse(self, response):
        re_selector = response.xpath("/html/ body/ div[@id='wrapper']/ div[@class='grid-8']/ div[1]/ div[1]/ h1")  #
        pass
