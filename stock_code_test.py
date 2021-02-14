
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time


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



# 현재 시간을 초 단위로 나타냄 // 86400을 통해 일 단위로 변환
time = int(time.time() // 86400)

print(time*86400)

# 1613288385
# 1613088000 / 86400 -> 18670일 -> 2월 14일 //하루는 86400초

# 일 단위 날짜에 따른 종가 저장  -> 나중엔 이 data를 어딘가에 저장해야함
for i in range(40):
    # 날짜에 따른 종가 출력
    try:
        date = soup.find("td", attrs={'data-real-value':'{}'.format(time*86400 - (i*86400))})
        price = date.find_next_sibling("td")
        print(date.text)
        print(price.text)
    # 휴장 하는 날은 제외
    except:
        None



