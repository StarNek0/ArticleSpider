# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/9/23 11:04'
# __sys__ = 'Windows 10'

import re

import scrapy
from scrapy.http import Request
import urlparse

from ArticleSpider.items import JobBoleArticleItem
from ArticleSpider.utils.common import get_md5
# urlparse是py2的，py3中是urllib.parse


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1.获取文章列表页中的具体文章URL，并交给scrapy下载后进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        :param response:
        :return:
        """

        # 解析列表页中的所有文章url并交给scrapy下载后进行解析
        # blog列表页的所有需要的url如下
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # 使用yield，然后scrapy自动下载
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=urlparse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)
                                    # 此处urljoin可以分辨该url是否是完整的URL

        # 提取下一页并交给scrapy进行下载
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_urls:
            yield Request(url=urlparse.urljoin(response.url, next_urls), callback=self.parse)


    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图片, get()避免抛出异常
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]

        create_dat = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0]
        create_date = re.findall(r'\d+/\d+/\d+', create_dat)[0]

        praise_nums = response.xpath("//div[@class='post-adds']/span[1]/h10/text()").extract()[0]

        # 收藏数提取
        shoucang = response.xpath(
            "//span[@class=' btn-bluet-bigger href-style bookmark-btn  register-user-only ']/text()").extract()[0]
        fav_nums = re.search('\d', shoucang)
        if fav_nums is not None:
            fav_nums = fav_nums.group()
        else:
            fav_nums = 0

        # 评论数提取
        pinglun = response.xpath("//span[@class='btn-bluet-bigger href-style hide-on-480']/text()").extract()[0]
        comment_nums = re.search('\d', pinglun)
        if comment_nums is not None:
            comment_nums = comment_nums.group()
        else:
            comment_nums = 0

        article = response.xpath("//div[@class='entry']").extract()
        # print article[0]

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [tag for tag in tag_list if not tag.strip().endswith(u'评论')]
        tags = ','.join(tag_list)


        article_item["title"] = title

        from datetime import datetime
        try:
            create_date = datetime.strptime(create_date, "%Y/%m/%d").date()
        except:
            create_date = datetime.now()
        article_item["create_date"] = create_date
        article_item["url"] = response.url
        article_item["url_object_id"] = get_md5(response.url)
        article_item["front_image_url"] = [front_image_url]
        article_item["front_image_path"] = None
        article_item["parise_nums"] = praise_nums
        article_item["comment_nums"] = comment_nums
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = article

        yield article_item

        # print tags
        # print("title:"), title
        # print("create_date:"), create_date
        # print("praise_nums:"), praise_nums
        # print("fav_nums:"), fav_nums
        # print("comment_nums:"), comment_nums
        # print("article:"), article
        # print("tags:"), tags
        pass
