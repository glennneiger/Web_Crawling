import urllib.request
from bs4 import BeautifulSoup


#크롤링, url을가져오고 그것을 분석한다음에, 분석을 한것에서 원하는 것만 저장


url= 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

html=urllib.request.urlopen(url).read() #html을 가져올수있다.

soup = BeautifulSoup(html,'html.parser') #뷰티풀숩으로 분석. 여기까지 기본적 준비끝


#네이버 블로그 검색시 나오는 타이틀과 url을 전부 가져올것임

title=soup.find_all(class_='sh_blog_title') #네이버 블로그제목에 들어있는클래스(f12로 확인)

#print(len(title)) #블로그탭에 나온 갯수 10개




for i in title:
    print(i.attrs['title'])  #attrs를 넣으면 속성값을 볼수있음
    print(i.attrs['href'])
    print()


#위 코드는 url을 고정으로 넣었음. (문제점)


#출처
#https://www.youtube.com/watch?v=hKApZHK_fOQ





