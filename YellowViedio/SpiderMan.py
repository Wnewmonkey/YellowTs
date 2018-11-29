import os


from YellowViedio.HtmlParser import HtmlParser
from YellowViedio.UrlManager import UrlManager
from YellowViedio.HtmlDownloader import  HtmlDownloader
from urllib import parse
from YellowViedio.OutPut import Download

from multiprocessing import Process
class SpiderMan(object):
    def __init__(self):
        self.download = HtmlDownloader()
        self.parser = HtmlParser()
        self.manager = UrlManager()
        self.down = Download()

    def crawl(self,url):
        #通过永久域名获得当前域名
        real_root_url,root_url = self.download.real_root_url(url)   #https://www.4455ne.com/enter/pc.html
        root_html = self.download.download(real_root_url)
        url = self.parser.real_root_url(root_html,root_url)     #https://www.4455ne.com/index/home.html
        #解析url得到亚洲情色的href和title并输入数字选择分组
        html = self.download.download(url)
        href,title = self.parser.parser(html,root_url)      #得到影片分类以及分类地址
        self.manager.add_top_url(href, title)
        for i in self.manager.title:
            print(i)
        num = input('请输入对应数字：')
        qingse_url = self.manager.href[int(num)-1]
        qingse_url = qingse_url[:-9]+parse.quote(qingse_url[-9:-5])+qingse_url[-5:]     #https://www.4455ne.com/shipin/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1.html
        href1,name = self.parser.parser1(self.download.download(qingse_url),root_url)
        self.manager.add_href_name(href1,name)
        for i in self.manager.name:
            print(i)
        num = input('请输入影片对应的数字：')
        av_url = self.manager.href1[int(num)-1]
        #print(av_url)       #https://www.4455ne.com/shipin/36050.html
        av_url = self.parser.parser2(self.download.download(av_url),root_url)
        #print(av_url)       #https://www.4455ne.com/shipin/play-36050.html?road=1
        huang_url = self.parser.parser3(self.download.download(av_url))
        #self.m3u8.getVideo_requests(huang_url)
        #self.output.url_open(huang_url,self.manager.name[int(num)-1])
        sum = self.down.sum(huang_url+'.m3u8')
        i=sum
        name = self.manager.name[int(num)-1][2:]

        huang_url = huang_url + '.m3u8'

        if not os.path.exists('D:\\AV\\'):
            os.chdir('D:\\')
            os.mkdir('D:\\AV')
            os.chdir('D:\\AV')
            os.mkdir('D:\\AV'+'\\'+name)
            os.chdir('D:\\AV'+'\\'+name)
        else:
            os.chdir('D:\\AV')
            if not os.path.exists('D:\\AV' + '\\' + name):
                os.mkdir('D:\\AV' + '\\' + name)
                os.chdir('D:\\AV' + '\\' + name)
            else:
                os.chdir('D:\\AV' + '\\' + name)

        p1 = Process(target=self.down.down, args=(huang_url,0, (i - 1) // 3,name,))  # 申请子进程
        p2 = Process(target=self.down.down, args=(huang_url,(i - 1) // 3 + 1, (i - 1) // 3 * 2,name,))
        p3 = Process(target=self.down.down, args=(huang_url,(i - 1) // 3 * 2 + 1, i,name,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        self.down.move(i,name)
if __name__=='__main__':

    spider = SpiderMan()
    print('欢迎使用自动AV下载系统^_^'+'\n'+'请选择你要观看的AV类型，并输入对应数字')
    url = 'https://www.4455YC.com'
    spider.crawl(url)
