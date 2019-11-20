import urllib.request

import urllib.parse 


from bs4 import BeautifulSoup



url='https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20191120&page=1'


html=urllib.request.urlopen(url).read() 

bs_obj = BeautifulSoup(html,'html.parser') 


step1=bs_obj.select('div.list_body.newsflash_body > ul > li > dl > dt > a')

# print(step1)


for step in step1:
    print(step.text.strip()) #텍스트 부분을 출력후 ,strip 으로 없앤 부분 공백 제거
    print(step.get('href'))

