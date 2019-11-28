
import urllib.request
import requests
import urllib.parse 
from bs4 import BeautifulSoup

url='https://www.naver.com/'

reponse= requests.get(url)  #HTML소스를 String으로 변환시켜서 변수에 저장시켜주는 역할 - requests

source= reponse.text
soup=BeautifulSoup(source,'html.parser')


# print(soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'))

top_list=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

print(len(top_list))

for top in top_list:
    print(top.text)


# https://l0o02.github.io/2018/06/10/python-crawling-2/

