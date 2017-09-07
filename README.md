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


## 使い方

### Scrapyのインストール

    $ pip install Scrapy

### ダウンロード

    $ git clone https://github.com/kakawup/WUBlogImgDownloader.git


### 実行

    $ cd WUGBlog
    $ scrapy crawl [WUGBlog | RGRBlog] -o BLOG_IMAGE.json
    $ cd ..
    $ python downloader.py WUGBlog/BLOG_IMAGE.json [WUG | RGR]

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

### 設定

./WUGBlog/WUGBlog/settings.py

```python:settings.py
DOWNLOAD_DELAY = 3   # クロール間隔 [s]
CONFIG = {
    "WUG": {
        "name_list": ["mayu", "airi", "minami", "yoshino", "nanami", "kaya", "miyu"],   # 保存先ディレクトリ名
        "start_url": ["https://ameblo.jp/wakeupgirls/entry-11600411806.html"],          # アクセス開始ページ
        "start_member": 0                                                               # 開始ページの担当
    },
    "RGR": {
        ...
    }
}
```
