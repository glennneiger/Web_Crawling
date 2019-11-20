import urllib.request

import urllib.parse 


from bs4 import BeautifulSoup



url='https://news.naver.com/'


html=urllib.request.urlopen(url).read() 

bs_obj = BeautifulSoup(html,'html.parser') 

step1=bs_obj.find("ul",{'class':'section_list_ranking'})
step2=step1.findAll('li')

for li in step2:
    a_all=li.find('a')
    print(a_all.text)



# for i in first:
#     print(i.text.strip())

