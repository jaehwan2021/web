
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime


#url 기반 웹 크롤링
url = 'https://www.investing.com/equities/jp-morgan-chase-historical-data'

#서버 접속간 사용자 고유 코드 (구글에 what is my user agent 검색 및 복붙해서 사용할 것)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}

#해당 url을 user-agent 정보를 통해 가져옴
req = requests.get(url, headers=headers)

# req가 비정상적으로 가져와질 경우 code종료
req.raise_for_status()

#req해온 text를 파싱해서 soup란 객체에 저장
soup = BeautifulSoup(req.text, 'html.parser')




#작업중

time = input()

#18667 = 2월 9일

date = soup.find("td", attrs={'data-real-value':'{}'.format(time)})
price = date.find_next_sibling("td")

print(date.text)
print(price.text)



#sdfsdf
#test


#dsf