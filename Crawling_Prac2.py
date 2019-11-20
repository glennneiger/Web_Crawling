import urllib.request

import urllib.parse 


from bs4 import BeautifulSoup



url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn'


html=urllib.request.urlopen(url).read() 

soup = BeautifulSoup(html,'html.parser') 

first=soup.find_all('div',{'class':'tit3'})



for i in first:
    print(i.text.strip())

