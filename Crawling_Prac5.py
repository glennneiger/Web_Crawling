import urllib.request

import urllib.parse 
from bs4 import BeautifulSoup

url='https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20191120&page=1'
html=urllib.request.urlopen(url).read() 

bs_obj = BeautifulSoup(html,'html.parser') 
<<<<<<< HEAD
step1=bs_obj.select('div.list_body.newsflash_body > ul > li > dl')

a=[]

for step in step1:
    a = step.find_all('a') # 리스트 a 에다가 step1 하위에 속한 태그 a 값들을 넣고
    
    



    for b in a: #for문으로 차례로 출력
        print(b.text.strip())
        
      

    if(len(a)>0):        
        print(a[0].get('href'))

   


