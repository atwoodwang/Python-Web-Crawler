from urllib import request

class HtmlOutputer(object):
    def __init__(self):
        self.count=1
    def download_image(self, links):
        for link in links:
            with request.urlopen(link) as f:
                if f.status!=200:
                    continue
                image_content=f.read()
                fout=open('%d.jpg'%self.count,'wb')
                fout.write(image_content)
                print('Downloaded from %s. Total: %d' %(link,self.count))
                self.count+=1
