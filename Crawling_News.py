import urllib.request
import requests
import urllib.parse #url 변환시, 한글이 인식안되는 문제를 해결하기위한 import


from bs4 import BeautifulSoup

Baseurl='https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=230&sid1=105&date=20191125&page='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page=input('페이지 : ')
print()


Url=Baseurl+page
html=requests.get(Url,headers=headers).text
soup=BeautifulSoup(html,'html.parser')




Title=soup.select('div.content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2)')



print(Title)


for a in Title:
    
    
    print(a.text.strip())

    print(a.get('href'))

   



    

        



   

