from urllib import parse
from bs4 import BeautifulSoup

import html_downloader
import html_parser
import sys


class Movie_Search(object):
    def __init__(self,title):
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.title=title

    def search(self):
        try:
            movie=parse.quote(self.title)
            movie_search_url="http://movie.douban.com/subject_search?search_text="+movie+"&cat=1002"
            movie_search_html=self.downloader.download(movie_search_url)
            movie_url=self.parser.parse_movie(movie_search_html)
            movie_html=self.downloader.download(movie_url)
            self.parser.parse_data(movie_html)
        except:
            print('Failed: No such a movie or No internet')

def main(argv):
    try:
        title=argv[1]
    except IndexError:
        print("Usage: python movie_search.py [Movie Title]")
        sys.exit()
    movie_search=Movie_Search(title)
    movie_search.search()

if __name__=='__main__':
    main(sys.argv)