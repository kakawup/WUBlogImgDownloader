# -*- coding: utf-8 -*-

# Target
BOT_NAME         = "WUGBlog"
SPIDER_MODULES   = ["WUGBlog.spiders"]
NEWSPIDER_MODULE = "WUGBlog.spiders"


# Base
ROBOTSTXT_OBEY  = True
COOKIES_ENABLED = False


# User Setting
DOWNLOAD_DELAY  = 3

CONFIG = {
    "WUG": {
        "name_list": ["mayu", "airi", "minami", "yoshino", "nanami", "kaya", "miyu"],
        "start_url": ["https://ameblo.jp/wakeupgirls/entry-11600411806.html"],
        "start_member": 0
    },
    "RGR": {
        "name_list": ["koko", "yuka", "atsugi"],
        "start_url": ["https://ameblo.jp/rungirlsrun/entry-12297485190.html"],
        "start_member": 0
    }
}