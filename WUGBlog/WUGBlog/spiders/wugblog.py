#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request
from WUGBlog.items import BlogImage

import re


# ==================================================
#   Base Parse Function
# ==================================================

class BaseBlog(CrawlSpider):
    def parse(self, response):
        # Next page
        next_page = response.css(".skin-pagingPrev::attr('href')").extract()
        if next_page:
            yield Request("https:" + next_page[0], self.parse)

        # Get all images
        imgs = response.css("a.detailOn > img::attr('src')").extract()
        imgs += response.css(".skin-entryBody div > img::attr('src')").extract()

        # Ignore [Staff's page] or [No image page]
        if (response.css(".skin-entryThemes a::text").extract()[0] == u"スタッフブログ") or (not imgs):
            yield None
        else:
            for index, img in enumerate(imgs):
                # Change Original Size
                for mat in re.compile("t0(.*?)_").finditer(img):
                    img = img.replace(mat.group(0), "o")

                try:
                    # Get date
                    DATE_PAT = re.compile("https://stat.ameba.jp/user_images/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)")
                    date = DATE_PAT.findall(img)[0]

                    # Set blog data
                    item = BlogImage()
                    item["title"]  = date[0] + date[1] + "-" + str(index) + ".jpg"
                    item["path"]   = img
                    item["author"] = self.name_list[self.page_counter % self.member_num]

                    yield item
                except IndexError:
                    yield None

            # Next Page
            self.page_counter += 1


# ==================================================
#   Blog for [Wake Up, Girls!]
# ==================================================

class WUGBlog(BaseBlog):
    name         = "WUGBlog"
    member_num   = 7

    # User Setting
    name_list    = ["mayu", "airi", "minami", "yoshino", "nanami", "kaya", "miyu"]
    start_urls   = ["https://ameblo.jp/wakeupgirls/entry-11600411806.html"]
    page_counter = 0


# ==================================================
#   Blog for [Run Girls, Run!]
# ==================================================

class RGRBlog(BaseBlog):
    name         = "RGRBlog"
    member_num   = 3

    # User Setting
    name_list    = ["koko", "yuka", "atsugi"]
    start_urls   = ["https://ameblo.jp/rungirlsrun/entry-12297485190.html"]
    page_counter = 0
