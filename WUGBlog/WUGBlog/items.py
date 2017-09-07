# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class BlogImage(Item):
    title  = Field()
    path   = Field()
    author = Field()
    pass
