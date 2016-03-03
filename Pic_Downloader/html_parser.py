import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/p/2369602689\?pn=\d+"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        new_pics=set()
        links=soup.find_all('img',class_='BDE_Image')
        for link in links:
            pic_url=link['src']
            new_pics.add(pic_url)
        return new_pics
