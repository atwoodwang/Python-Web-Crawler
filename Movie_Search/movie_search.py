from urllib import parse
from bs4 import BeautifulSoup

import html_downloader
import html_parser


class Movie_Search(object):
    def __init__(self):
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()

    def search(self):
        try:
            raw_input=input('What is the name of the movie: ')
            movie=parse.quote(raw_input)
            movie_search_url="http://movie.douban.com/subject_search?search_text="+movie+"&cat=1002"
            movie_search_html=self.downloader.download(movie_search_url)
            movie_url=self.parser.parse_movie(movie_search_html)
            movie_html=self.downloader.download(movie_url)
            self.parser.parse_data(movie_html)
        except:
            print('Failed: No such a movie or No internet')


if __name__=='__main__':
    movie_search=Movie_Search()
    movie_search.search()
