import sys

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()


    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s' % (count,new_url))
                html_cont=self.downloader.download(new_url)
                new_urls,new_pics = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.download_image(new_pics)

                if count==10:
                    break
                count+=1

            except:
                print('craw failed')

def main(argv):
    try:
        root_url=argv[1]
    except IndexError:
        print("Usage: python spider_main.py [URL]")
        sys.exit()
    root_url+='?pn=1'
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)

if __name__=='__main__':
    main(sys.argv)