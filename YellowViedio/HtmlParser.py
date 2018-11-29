

from bs4 import BeautifulSoup
import re
class HtmlParser(object):

    def parser(self,response,root_url):

        title = []
        href = []
        soup = BeautifulSoup(response, 'html.parser')
        a = soup.find_all('a',href = re.compile('shipin'))
        j=1

        for i in a[0:7]:
            title.append(str(j)+'、'+i.text)
            href.append(root_url[:-1]+i['href'])
            j+=1
        return href,title


    def real_root_url(self, html,url):
        soup1 = BeautifulSoup(html, 'html.parser')
        a = soup1.find_all('a', attrs={'class':'c_red'})
        return url[:-1]+a[0]['href']

    def parser1(self,response,root_url):
        href = []
        name = []
        soup = BeautifulSoup(response, 'html.parser')
        a = soup.find_all('a',href = re.compile('shipin'))
        for c in a[9:29]:
            href.append(root_url[:-1]+c['href'])
            name.append(c['title'])
        return href,name
    def parser2(self,response,root_url):
        soup = BeautifulSoup(response, 'html.parser')
        a = soup.find_all('a',attrs={'title':'线路一'})

        return root_url[:-1]+a[0]['href']

    def parser3(self,response):
        soup = BeautifulSoup(response, 'html.parser')
        a = soup.find('script')

        c = str(a).split("'")
        return  c[3]+c[1][:-5]



