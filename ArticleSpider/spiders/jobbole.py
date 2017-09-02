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

        praise_nums = response.xpath("//div[@class='post-adds']/span[1]/h10/text()").extract()[0]

        shoucang = response.xpath(
            "//span[@class=' btn-bluet-bigger href-style bookmark-btn  register-user-only ']/text()").extract()[0]
        fav_nums = re.search('\d', shoucang).group()

        pinglun = response.xpath("//span[@class='btn-bluet-bigger href-style hide-on-480']/text()").extract()[0]
        comment_nums = re.search('\d', pinglun).group()

        article = response.xpath("//div[@class='entry']").extract()
        print article[0]
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [tag for tag in tag_list if not tag.strip().endswith(u'评论')]
        tags = ','.join(tag_list)
        print tags

        title = response.css(".entry-header h1::text").extract()[0]
        print title
        pass
