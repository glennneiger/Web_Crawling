import time


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

url=input('댓글을 수집할 사이트 주소 입력 : ')

# url='https://sports.news.naver.com/news.nhn?oid=139&aid=0002123588&m_view=1&sort=LIKE'

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)



scroll=10

all= driver.find_element_by_tag_name('body')

time.sleep(2)

while scroll:
    
    all.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    scroll-=1
    
  
Id_list=[]
Contents_list=[]


id_contents=driver.find_elements_by_xpath('//*[@id="author-text"]/span')

Contents= driver.find_elements_by_id('content-text')

for temp in id_contents:
    Id_list.append(temp.text)

for temp in Contents:
    Contents_list.append(temp.text)

for number in range(len(Contents_list)):
    print(str(number+1) , ".   [ " + Id_list[number] + " ] ,  작성내용 -> [ " + Contents_list[number]+ " ]")
    print()
    print()



# 댓글 검색 프로그래밍 ㄱ

