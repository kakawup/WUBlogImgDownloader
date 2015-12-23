# WUBlog Image Downloader

## 概要

声優ユニット[Wake Up, Girls!](http://wug-portal.jp/)7人のメンバーが,
曜日ごとに更新している[オフィシャルブログ](http://ameblo.jp/wakeupgirls/)に投稿した写真をダウンロードしてくれるやつです.


## 環境

+ Python: 2.7.6
+ Scrapy: 1.0.3

### Scrapyのインストール

    $ pip install Scrapy


## 使い方

    $ cd WUGBlog
    $ scrapy crawl WUGBlog -o wugblog.json
    $ cd ..
    $ python downloader.py WUGBlog/wugblog.json WUG

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
