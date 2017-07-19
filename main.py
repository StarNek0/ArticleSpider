# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/7/19 16:35'
# __sys__ = 'Windows 10'

import sys
import os
from scrapy.cmdline import execute

# sys.path.append("E:/SpiderProject/ArticleSpider")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # dirname获取父目录，abspath获取当前文件路径
execute(["scrapy", "crawl", "jobbole"])

print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))