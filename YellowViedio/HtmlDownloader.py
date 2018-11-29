import urllib.request
class HtmlDownloader(object):
    def real_root_url(self,url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        response = urllib.request.urlopen(req)

        return response.geturl()+'enter/pc.html',response.geturl()

    def download(self,url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        return html



