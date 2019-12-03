import urllib.request

import urllib.parse 
from bs4 import BeautifulSoup

url='https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20191120&page=1'
html=urllib.request.urlopen(url).read() 

bs_obj = BeautifulSoup(html,'html.parser') 

step1=bs_obj.select('div.list_body.newsflash_body > ul > li > dl ')

count=0





for step in step1:
    a = step.find_all('a')

    for b in a: #for문으로 차례로 출력
        print(b.text.strip())
        
    if (len(a) > 0):
        print(a[0].get("href"))

