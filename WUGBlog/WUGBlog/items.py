# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class PageImgItem(Item):
    title  = Field()
    path   = Field()
    author = Field()
    pass
