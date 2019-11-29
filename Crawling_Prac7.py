import urllib.request
import requests
import urllib.parse 
from bs4 import BeautifulSoup

url='https://datalab.naver.com/keyword/realtimeList.naver?where=main'
reponse= requests.get(url)  #HTML소스를 String으로 변환시켜서 변수에 저장시켜주는 역할 - requests

source= reponse.text
soup=BeautifulSoup(source,'html.parser')



step1=soup.select('#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li > a > span.title')

print(len(step1))
