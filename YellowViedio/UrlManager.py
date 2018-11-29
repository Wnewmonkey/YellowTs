class UrlManager(object):
    def __init__(self):
        self.href = []
        self.title = []
        self.name = []
        self.href1 = []
    def add_top_url(self,href,title):
        for i in href:
            self.href.append(i)
        for j in title:
            self.title.append(j)
    def add_href_name(self,href,name):
        for i in href:
            self.href1.append(i)
        k=1
        for j in name:
            self.name.append(str(k)+'、'+j)
            k=k+1
    def has_url(self):
        return len(self.href)

    def get_url(self,a):
        return self.href.pop(int(a)-1)