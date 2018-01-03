# coding:utf8
"""
--------------------------------------------------------------------------
    File:   selenium_spider.py
    Auth:   zsdostar
    Date:   2018/1/3 21:29
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

from selenium import webdriver
from scrapy.selector import Selector


browser = webdriver.Chrome(executable_path='../ArticleSpider/spiders/chromedriver.exe')  # 这个exe是selenium的Chrome驱动

browser.get('https://www.zhihu.com/')# 打开浏览器及其网页
# print browser.page_source  # 打印F12的HTML代码

# 模拟输入用户名密码
browser.find_element_by_css_selector(".Input-wrapper input[name='username']").send_keys('18846030787')
browser.find_element_by_css_selector(".Input-wrapper input[name='password']").send_keys('klxsxzsdf1')
# 模拟点击
browser.find_element_by_css_selector(".SignFlow-submitButton").click()

t_seletor = Selector(text=browser.page_source)  # 将整个HTML传到Scrapy的selector里
# print t_seletor.css('.tm-promo-price .tm-price::text').extract()  # css选择器获取tmall价格


browser.quit()  # 手动关浏览器是不好使的，还会在任务栏待很久