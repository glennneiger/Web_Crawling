import urllib.request
import requests
import urllib.parse #url 변환시, 한글이 인식안되는 문제를 해결하기위한 import
import json

from bs4 import BeautifulSoup

# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler-With-Login/   참고

sess = requests.session()



req_url = 'https://sports.news.naver.com/wfootball/news/list.nhn?page=1&isphoto=N&view'

#f12 네트워크 기록후에 , 컨트롤 에프로 기사제목 검색하면 하나뜸, 그리고 그것의 header찾기

#html 소스가져오기
req2 = sess.get(req_url,headers={'user-agent':'nvsch'})


#req2라는 바이트배열을 디코딩하여 문자열데이터로 변환 , 그걸 loads
j_res = json.loads(req2.content.decode()) 



for number,step in enumerate(j_res['list'],1):
    print(number," : ",step['title'])


