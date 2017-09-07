# WUBlog Image Downloader

## 概要

声優ユニット[Wake Up, Girls!](http://wug-portal.jp/)7人のメンバー及び，
同じく声優ユニット[Run Girls, Run!](http://rungirlsrun.jp/)が，
曜日ごとに更新しているオフィシャルブログに投稿した写真をダウンロードしてくれるやつです．

+ [Wake Up, Girls! Official Blog](https://ameblo.jp/wakeupgirls/)
+ [Run Girls, Run! Official Blog](https://ameblo.jp/rungirlsrun/)


## 環境

+ Python: 2.7.6
+ Scrapy: 1.0.3


### Scrapyのインストール

    $ pip install Scrapy


## 使い方

    $ git clone https://github.com/kakawup/WUBlogImgDownloader.git
    $ cd WUGBlog
    $ scrapy crawl [WUGBlog | RGRBlog] -o BLOG_IMAGE.json
    $ cd ..
    $ python downloader.py WUGBlog/BLOG_IMAGE.json [WUG | RGR]

これでデフォルトなら

    $ tree WUG
    WUG
    ├── airi
    │   └── ***.jpg
    ├── kaya
    │   └── ***.jpg
    ├── mayu
    │   └── ***.jpg
    ├── minami
    │   └── ***.jpg
    ├── miyu
    │   └── ***.jpg
    ├── nanami
    │   └── ***.jpg
    └── yoshino
        └── ***.jpg

みたいに画像が保存される.

各メンバーごとの保存先ディレクトリ名やファイル名のフォーマットは `WUGBlog/WUGBlog/spiders/wugblog.py` で変更できます.
