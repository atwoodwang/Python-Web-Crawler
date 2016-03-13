# Python-Web-Crawler
一些小的爬虫脚本 纯属无聊的产物。。。

## Dependencies
为了正常运行 需要先安装BeautifulSoup4库 

下载和安装请看： [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#)


## Baike Spider
能够定量爬取百度百科某一页面和与其相关的词条 并将词条的标题和简介整理成一个html网页保存 默认抓取30个网页
###Usage
```
$ python spider_main.py [URL]
```

example:

```
$ python spider_main.py http://baike.baidu.com/view/21087.htm
```

## Movie Search
利用豆瓣电影API 获取某一电影的详细信息

###Usage
```
$ python movie_search.py [Movie Title]
```

example:

```
$ python movie_search.py 疯狂动物城
```

## Pic Downloader
下载某一百度贴吧帖子中的图片
比如 [这个帖子](http://tieba.baidu.com/p/4245404663)里所有图片 包括后续页面中的图片

###Usage
```
$ python spider_main.py [URL]
```

example:

```
$ python spider_main.py http://tieba.baidu.com/p/4245404663
```