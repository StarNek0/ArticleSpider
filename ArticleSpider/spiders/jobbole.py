# -*- coding: utf-8 -*-
# 产生这个文件的命令为项目根目录下scrapy genspider jobbole blog.jobbole.com
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/111865/']

    def parse(self, response):
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]

        create_dat = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0]
        create_date = re.findall(r'\d+/\d+/\d+', create_dat)[0]

        zan = response.xpath("//div[@class='post-adds']/span[1]/h10/text()").extract()[0]

        shoucan = response.xpath("//span[@class=' btn-bluet-bigger href-style bookmark-btn  register-user-only ']/text()").extract()[0]
        shoucang = re.search('\d', shoucan).group()

        pinglu = response.xpath("//span[@class='btn-bluet-bigger href-style hide-on-480']/text()").extract()[0]
        pinglun = re.search('\d', pinglu).group()
        pass