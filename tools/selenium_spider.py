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

browser = webdriver.Chrome(executable_path='chromedriver.exe')  # 这个exe是selenium的Chrome驱动
browser.get('https://www.baidu.com')
print browser.page_source