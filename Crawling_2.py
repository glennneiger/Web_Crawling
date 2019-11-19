import urllib.request

import urllib.parse #url 변환시, 한글이 인식안되는 문제를 해결하기위한 import


from bs4 import BeautifulSoup


#1코드와 달리 베이스가 될 url을 정해놓고, 추가 url을 덧붙여서 그 url을 검색하는 방식으로 코딩


baseurl= 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='

plusUrl=input('검색어를 입력하세요 : ')

url=baseurl+urllib.parse.quote_plus(plusUrl) #urllib을 통해 한글 검색부분을 알맞게 변환하여(코드로) 출력


html=urllib.request.urlopen(url).read() 

soup = BeautifulSoup(html,'html.parser') 



title=soup.find_all(class_='sh_blog_title') 



for i in title:
    print(i.attrs['title'])  
    print(i.attrs['href'])
    print()





#출처
# https://www.youtube.com/watch?v=OEf_UESjRxo





