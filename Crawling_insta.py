from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time 


# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/



baseUrl='https://www.instagram.com/explore/tags/'
plusUrl=input('검색할 태그를 입력하세요.')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3) 
 
html = driver.page_source #드라이버로 페이지 소스를 통해 담는다

soup=BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w') # 공백을 다 없애주고 클래스가 3개이므로 . 으로 구분

n=1

for i in insta:
    print('https://www.instagram.com'+i.a['href'])
    imgUrl=i.select_one('.KL4Bh').img['src'] # selcet_one으로 KL4Bh를 가져오고 거기서 img안의 src를 찾는다
    with urlopen(imgUrl) as f:
        with open('./img/'+plusUrl + str(n)+'.jpg','wb') as h: #open은 파일이없을경우 생성하는 명령어  -> img 폴더에 , 태그 + 숫자넘버 . jpg 형태의 이름으로 저장. wb -> 바이너리파일
            img = f.read() #read함수는 파일의 내용 전체를 문자열로 돌려준다.
            h.write(img) # 생성과 동시에 문자열을 바이너리로 저장 -> 사진이 나옴
            

    n +=1
    print(imgUrl)
    print()


driver.close()

