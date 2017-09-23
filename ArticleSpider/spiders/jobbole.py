# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/9/23 11:04'
# __sys__ = 'Windows 10'

import re
import scrapy
from scrapy.http import Request
from .last_jobbole import parse_detail
import urlparse
# urlparse是py2的，py3中是urllib.parse


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        """
        1.获取文章列表页中的具体文章URL，并交给scrapy下载后进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        :param response:
        :return:
        """

        # 解析列表页中的所有文章url并交给scrapy下载后进行解析
        # blog列表页的所有需要的url如下
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            # 使用yield，然后scrapy自动下载
            yield Request(url=urlparse.urljoin(response.url, post_url), callback=parse_detail)

        # 提取下一页并交给scrapy进行下载