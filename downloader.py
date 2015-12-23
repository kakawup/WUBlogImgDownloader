#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import os
import urllib2
import json


def imgDownload(url, outfile):
    if not os.path.exists(os.path.dirname(outfile)):
        os.makedirs(os.path.dirname(outfile))

    opener = urllib2.urlopen(url)
    img = open(outfile, "wb")
    img.write(opener.read())
    opener.close()
    img.close()


if __name__ == "__main__":
    if len(argv) == 3:
        JSON_FILE = argv[1]
        IMG_DIR   = argv[2]
    else:
        print "[Usage] python downloader.py JSON_FILE OUT_DIR"
        quit()

    if not os.path.exists(JSON_FILE):
        print "'%s' doesn't exist..." % JSON_FILE
        quit()

    with open(JSON_FILE, "r") as file:
        imgs = json.load(file)
        for img in imgs:
            imgDownload(img["path"], "%s/%s/%s" % (IMG_DIR, img["author"], img["title"]))
            print "[ %-7s ]: %s" % (img["author"], img["title"])
