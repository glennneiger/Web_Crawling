import time


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions


url='https://sports.news.naver.com/news.nhn?oid=139&aid=0002123588&m_view=1&sort=LIKE'

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

while True:
    try:
        더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        더보기.click()
        time.sleep(1)
    
    except :
        break

#element에 s 를 붙여줌
contents= driver.find_elements_by_css_selector('span.u_cbox_contents')

for number,content in enumerate(contents,1) :
    print(number, " : ",content.text)

#댓글내용수집