import time


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions

url=input('댓글을 수집할 사이트 주소 입력 : ')

# url='https://sports.news.naver.com/news.nhn?oid=139&aid=0002123588&m_view=1&sort=LIKE'

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

Cd={}



while True:
    try : 
        
        all= driver.find_element_by_css_selector('a.u_cbox_btn_view_comment')
        all.click()
        time.sleep(1)

    except:
        break



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
    Cd[str(number)]=str(content.text)
    # print(number, " : ",content.text)


InputComment = input("찾고자하는 댓글 : ")
tempNumber=1

for i in Cd.values():

    temp=str(i)

    if temp.find(InputComment)>=0:
        print(tempNumber," : " +temp)
        print()
        tempNumber+=1

    
