# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
中国大学排名定向爬虫
@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import bs4

#获取源代码
def getHTMLText(url):	
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "获取失败"

#将源代码解析后存入ulist列表中	
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:	#遍历tbody标签的子标签
        if isinstance(tr,bs4.element.Tag):	#过滤子标签中字符串类
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    pass

#输出列表中前num项
def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
   
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
    
main()
