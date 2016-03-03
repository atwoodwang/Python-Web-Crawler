import re
from bs4 import BeautifulSoup
import json

class HtmlParser(object):
    def parse_movie(self, html):
        soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        movie_url=soup.find('a',href=re.compile(r"https://movie.douban.com/subject/\d+"))
        movie_id=re.split('\D+',movie_url['href'])
        movie_url="https://api.douban.com/v2/movie/"+movie_id[1]
        return movie_url

    def parse_data(self, html):
        data={}
        info=json.loads(html.decode('utf8'))
        print('标题: %s'%info['title'])
        print('评分:',info['rating']['average'])
        print('导演:','/ '.join(info['attrs']['director']))
        print('主演:','/ '.join(info['attrs']['cast']))
        print('类型:','/ '.join(info['attrs']['movie_type']))
        print('制片国家/地区:','/'.join(info['attrs']['country']))
        print('语言:','/ '.join(info['attrs']['language']))
        print('上映日期:','/'.join(info['attrs']['pubdate']))
        print('片长:','/'.join(info['attrs']['movie_duration']))
        print('简介:',info['summary'])
