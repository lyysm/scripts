'''
Author: liuyin
Date: 2022-08-06 22:20:54
LastEditTime: 2022-08-07 00:36:58
FilePath: /scripts/python/ba-wodl/get_news.py
Description: 新闻爬虫
'''
# -*- coding:UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup

PAGE_NUMBER = 100


def main():
    target = 'https://www.binancezh.top/en/news/top'
    url_list = [target]
    i = 1
    while i <= PAGE_NUMBER:
        url = target + "?page=" + str(i)
        url_list.append(url)
        i += 1
    for u in url_list:
        print("当前页:{}".format(u))
        req = requests.get(url=u)
        html = req.text
        bf = BeautifulSoup(html, features="lxml")
        a = bf.find_all('a')
        l = []
        for each in a:
            url = each.get('href')
            if '/en/news/top/' in url:
                l.append(url)

        l = list(set(l))
        for u in l:
            page = 'https://www.binancezh.top'+u
            id = u.split('/')[-1]
            savePage(page, id)
            time.sleep(1)


def savePage(page, id):
    print("下载{}".format(page))
    response = requests.get(page)
    bf = BeautifulSoup(response.text, features="lxml")
    a = bf.find_all('article')
    l = []
    for each in a:
        # print(each.text)
        file = open("pages/page-"+id+".txt", "w", encoding="utf")
        file.write(each.text)
        file.close()
    return


if __name__ == '__main__':
    main()