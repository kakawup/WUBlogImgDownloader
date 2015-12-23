#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.http.request import Request
from WUGBlog.items import PageImgItem

import re

NAME_LIST  = ["mayu", "airi", "minami", "yoshino", "nanami", "kaya", "miyu"]
CURRENT_ID = 0  # 開始記事の担当メンバーID (0~6)


class WUGBlog(CrawlSpider):
    name = "WUGBlog"

    # アメブロのWUGブログ内の個別記事ページのみを探索
    allowed_domains = ["ameblo.jp"]
    start_urls      = ["http://ameblo.jp/wakeupgirls/entry-11600411806.html"]

    # 担当者名用カウンタ
    pageCounter = CURRENT_ID


    def parse(self, response):
        # 次の記事へ
        nextPage = response.css(".skin-pagingPrev::attr('href')").extract()
        if nextPage:
            yield Request(nextPage[0], self.parse)

        # ページ内の画像を全て取得
        imgs = response.css("a.detailOn > img::attr('src')").extract()
        imgs += response.css(".skin-entryBody div > img::attr('src')").extract()

        # スタッフブログ | 画像がない場合は飛ばす
        if (response.css(".skin-entryThemes a::text").extract()[0] == u"スタッフブログ") or (not imgs):
            yield None
        else:
            for index, img in enumerate(imgs):
                # 圧縮版をオリジナルサイズに
                for mat in re.compile("t0(.*?)_").finditer(img):
                    img = img.replace(mat.group(0), "o")

                try:
                    # 日付データ取得
                    DATE_PAT = re.compile("http://stat.ameba.jp/user_images/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)/(.*?)")
                    date = DATE_PAT.findall(img)[0]

                    # データセット
                    item = PageImgItem()
                    item["title"]  = date[0] + date[1] + "-" + str(index) + ".jpg"  # ex) 2015122023-0.jpg
                    item["path"]   = img
                    item["author"] = NAME_LIST[self.pageCounter % 7]

                    yield item
                except IndexError:
                    yield None

            # 次の担当者へ
            self.pageCounter += 1
