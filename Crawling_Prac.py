import urllib.request

import urllib.parse 


from bs4 import BeautifulSoup



url='https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N'


html=urllib.request.urlopen(url).read() 

soup = BeautifulSoup(html,'html.parser') 



title=soup.select('#_ranking_news_list_0 span')

print(title)

for i, out in enumerate(title,1): #맨오른쪽의 1은 1부터 시작하라는 뜻
    print(i, out.text)


