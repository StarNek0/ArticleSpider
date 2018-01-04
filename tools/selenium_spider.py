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
import time

from selenium import webdriver
from scrapy.selector import Selector

# 设置ChromeDriver不加载图片
# 为什么这么写，因为Chrome配置文件是这个，里面可以搜到变量名字 C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Preferences
chrome_opt = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values":
        {
            "images":2,
            # "javascript":2
        }
}
chrome_opt.add_experimental_option("prefs", prefs)

# 知乎
# browser = webdriver.Chrome(executable_path='../ArticleSpider/spiders/chromedriver.exe')  # 这个exe是selenium的Chrome驱动
#
# browser.get('https://www.zhihu.com/')# 打开浏览器及其网页
# # print browser.page_source  # 打印F12的HTML代码
#
# # 模拟输入用户名密码
# browser.find_element_by_css_selector(".Input-wrapper input[name='username']").send_keys('18846030787')
# browser.find_element_by_css_selector(".Input-wrapper input[name='password']").send_keys('klxsxzsdf1')
# time.sleep(1.5)
# # 模拟点击
# browser.find_element_by_css_selector(".SignFlow-submitButton").click()
# time.sleep(1.5)
# t_seletor = Selector(text=browser.page_source)  # 将整个HTML传到Scrapy的selector里
# # print t_seletor.css('.tm-promo-price .tm-price::text').extract()  # css选择器获取tmall价格
#
# browser.quit()  # 手动关浏览器是不好使的，还会在任务栏待很久

# 微博
browser = webdriver.Chrome(executable_path='../ArticleSpider/spiders/chromedriver.exe', chrome_options=chrome_opt)  # 这个exe是selenium的Chrome驱动
# browser.get("https://www.taobao.com")
# time.sleep(5)
# browser.quit()

try:
    browser.get('https://weibo.com')
    time.sleep(7)
    browser.find_element_by_id('loginname').send_keys('18846030787')
    browser.find_element_by_css_selector(".info_list.password input[name='password']").send_keys('klxsxzsdf1')
    time.sleep(1)
    browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
    for i in xrange(2):
        time.sleep(3)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                           "var lenOfPage=document.body.scrollHeight;"
                           "return lenOfPage;")
finally:
    time.sleep(5)
    browser.quit()