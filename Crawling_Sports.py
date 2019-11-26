import urllib.request
import requests
import urllib.parse #url 변환시, 한글이 인식안되는 문제를 해결하기위한 import
import json

from bs4 import BeautifulSoup

# Baseurl='https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N&page='

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

# page=input('페이지 : ')
# print()


# Url=Baseurl+page
# html=requests.get(Url,headers=headers).text
# soup=BeautifulSoup(html,'html.parser')




# Title=soup.select('div.content')

# print(Title)

sess = requests.session()
req_url = 'https://sports.news.naver.com/wfootball/news/list.nhn?page=1&isphoto=N&view=photo'
req2 = sess.get(req_url,headers={'user-agent':'nvsch'})
print(req2.content.decode())
j_res = json.loads(req2.content.decode())
print(j_res)



