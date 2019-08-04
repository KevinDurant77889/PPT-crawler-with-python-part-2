# -*- coding: utf-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup
import os
import random

fake_agent = ['Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
         'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
         'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
         'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3' ,
         'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
         'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.',
         'User-Agent','Mozilla/5.0 (X11; NetBSD) AppleWebKit/547.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']



def download(url):
    req = urllib.request.urlopen("https://disp.cc/b/" + url)
    temp = req.read().decode()
    
    jpg_target = re.findall("https://imgur.com/\w\w\w\w\w\w.jpg", temp)
    jpg_target = list(set(jpg_target))
    
    jpg_target_2 = re.findall("https://i.imgur.com/\w\w\w\w\w\w\w.jpg", temp)
    jpg_target_2 = list(set(jpg_target_2))
    
    jpg_target.extend(jpg_target_2)
    if jpg_target == []:
        return 0
    soup = BeautifulSoup(temp,"html.parser")
    title = soup.find("pre").get_text()
    
    title = re.sub('[ ? , > , < , / , \\\\ , " , : , * ]', "", title)
    
    image_name = 1
    os.mkdir(title)
    for element in jpg_target:
        req = urllib.request.Request(element)
        req.add_header('User-Agent', random.choice(fake_agent))
        image_req = urllib.request.urlopen(req)
        image = image_req.read()
        with open(title + '\\' + str(image_name) + '.jpg', 'wb') as file:
            file.write(image)
        image_name+=1   


def FidePage(x):
    req = urllib.request.urlopen("https://disp.cc/b/Beauty?pn=" + str(x)+"&init=0")
    temp = req.read().decode()
    target = re.findall("62-\w\w\w\w", temp)
    urllist = list(set(target))
    return urllist


start = int(input("開始: "))
end = int(input("結束: "))
while(start < end):
    urllist = FidePage(start)
    for url in urllist:
        download(url)
    start += 20
