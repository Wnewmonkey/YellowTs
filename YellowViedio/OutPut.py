import urllib
import urllib.request, urllib.error, requests
import os
class Download(object):

    def sum(self,url):
        print('begin run ~~\n')
        videoName = url.split('/')[-2]

        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        urlData = urllib.request.urlopen(req)

        #path = r"D:\\AV\\aa\\"
        #tempName_video = os.path.join(path, '{}.ts'.format(videoName))  # f'{}' 相当于'{}'.format() 或 '%s'%videoName
        #open(tempName_video, "wb").close()  # 清空(顺带创建)tempName_video文件，防止中途停止，继续下载重复写入

        i = 0
        for line in urlData:
            # 解码decode("utf-8")，由于是直接使用了所抓取的链接内容，所以需要按行解码，如果提前解码则不能使用直接进行for循环，会报错
            url_ts = str(line.decode("utf-8")).strip()  # 重要：strip()，用来清除字符串前后存在的空格符和换行符
            if not '.ts' in url_ts:
                continue
            else:
                if not url_ts.startswith('http'):  # 判断字符串是否以'http'开头，如果不是则说明url链接不完整，需要拼接
                    # 拼接ts流视频的url
                    url_ts = url.replace(url.split('/')[-1], url_ts)


            i = i + 1
        i=i-1
        return i


    def down(self,url,a,b,name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        for i in range(a,b+1):
            c = url[0:-5]+str(i)+'.ts'

            response = requests.get(c, headers=headers)
            file = 'D:\\AV'+'\\'+name+'\\'+name+'_'+str(i) + ".ts"
            f = open(file, "ab+")
            f.write(response.content)
            if  a==0:
                print('已完成-->'+str(float('%.2f' % (i/b))*100)+'%')
        f.close()

    def move(self,num,name,path="D:\\AV\\"):
        os.chdir(path+name+'\\')
        f = open(path+name+'\\'+name+".ts", 'wb+')
        for i in range(0, num+1):
            filepath = path+name+r'\\'+name+'_'+"%d.ts"%(i)
            if os.path.exists(filepath):
                for line in open(filepath, 'rb'):
                    f.write(line)
                f.flush()
                os.remove(filepath)
        f.close()




