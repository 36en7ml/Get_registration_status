#coding:utf-8
import os
import re
import sys
from urllib.request import urlopen
from urllib.parse import urljoin
from html import unescape

base_url = 'http://web-int.u-aizu.ac.jp/official/students/sad/ML/Index/mlindex_j.html'

isMJH = False
isURL = False
ls = os.listdir("./")
for file in ls:
    if(file == 'mlindex_j.html'):
        isMJH = True
    if(file == 'url.txt'):
        isURL = True

if(isMJH == False and isURL == False):
    f = open('url.txt', 'w')
    f.close()
    os.system("wget " + base_url)
    url = os.system("cat mlindex_j.html | grep align=center | sed -E 's/<td align=center><a href=//' | sed -E 's/>■<\/a><\/td>//' > url.txt")
    os.remove("./mlindex_j.html")

fourl = open('url.txt', 'r')
line = fourl.readline()

print('特定対象の学籍番号を入力してください♪')
ID = input()

isFirst = True
while line:
    f = urlopen(urljoin(base_url, line))

    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)

    subject = re.search('科目名:.*', html).group(0)
    subject = subject.replace('科目名: ', '')
    subject = subject.replace('<br>', '')

    p = re.search('.*時限.*', html).group(0)
    p = p.replace('<br>', '')

    userid = re.search(ID, html)

    if(userid != None):
        if(isFirst):
            name = re.search(ID + '.*', html).group(0)
            name = name.replace(ID, '')
            #name = name.replace('</td><td>', ' ')
            name = name.replace('</td></tr>', ' ')
            name = name.split('</td><td>')

            print()
            print('あの人の学籍番号は分かっているのに、どんな講義を受講しているのか分からない...')
            print('そんな時、みなさんはどうしていますか？')
            print()
            print('学籍番号が分かっているなら履修科目も気になりますよね？')
            print('私も気になります！！')
            print()
            print('それでは今から、' + name[1] + 'さんの履修している科目一覧を表示したいと思います！')
            print()
            print()
            isFirst = False
        print(subject)
        print(p)
        print()

    line = fourl.readline()

print()
print('いかがでしたか？')
fourl.close()
f.close()
