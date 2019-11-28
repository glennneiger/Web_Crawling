import urllib.request
import requests
import urllib.parse 
from bs4 import BeautifulSoup

url='https://datalab.naver.com/keyword/realtimeList.naver?where=main'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
reponse = requests.get(url, headers = headers)

source= reponse.text
soup=BeautifulSoup(source,'html.parser')
step1=soup.select('#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li > a > span.title')




for number,step2 in enumerate(step1,1):
	print(number,step2.text)


