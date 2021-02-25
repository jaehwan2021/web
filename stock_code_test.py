
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time


import pymysql # mysql - python 연동 위한 import

def save(file_name, date, value): ## "file_name", list, list 형식의 data를 입력하면 마리아db에 해당 파일 이름의 date와 value열에 data가 자동으로 입력됨

    conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='pythondb',
                           charset='utf8')  ## 해당 db에 연결

    try:
        cur = conn.cursor()  ## 커서생성
        company_code = file_name  # table 이름 생성간 '-' 나 숫자 입력이 불가능함.. 일단 임시로 아무거나 적어둠
        sql = "CREATE TABLE IF NOT EXISTS " + company_code + "(date INT, value INT)"  # 파일 생성
        cur.execute(sql)  # 커서로sql 실행

        for i in range(len(date) - 1):

            sql = "insert into " + company_code + "(date, value) values (%s, %s)"
            cur.execute(sql, (date[i], value[i]))


        conn.commit()  ## 저장

    finally:  # database를 conn으로 연 후 항상 닫아주도록 finally 설정
        conn.close()

# https://www.investing.com/equities/ + "variable" + -historical-data 형태 url의 파싱한 data를 return하는 함수로 정의
def souping(company_name):

    #입력받은 변수를 함수정의에 사용하기 위해 임의의 변수에 저장
    data_save_company_name = company_name


    #url 기반 웹 크롤링
    url = 'https://www.investing.com/equities/{}-historical-data'.format(data_save_company_name)

    #서버 접속간 사용자 고유 코드 (구글에 what is my user agent 검색 및 복붙해서 사용할 것)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68"}

    #해당 url을 user-agent 정보를 통해 가져옴
    req = requests.get(url, headers=headers)

    # req가 비정상적으로 가져와질 경우 code종료
    req.raise_for_status()

    #req해온 text를 파싱해서 soup란 객체에 저장
    soup = BeautifulSoup(req.text, 'html.parser')

    return soup

# souping()는 원하는 회사명 입력하면 soup 객체 형태로 변환
# 추후 https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;{}.format("1~20") 여기서 회사이름 따올예정

soup = souping("apple-computer-inc")

# 현재 시간을 초 단위로 나타냄 // 86400을 통해 일 단위로 변환
time = int(time.time() // 86400)


# 1613288385
# 1613088000 / 86400 -> 18670일 -> 2월 14일 //하루는 86400초
soup.find("picker")
print(soup.text)
# 일 단위 날짜에 따른 종가 저장  -> 나중엔 이 data를 어딘가에 저장해야함

for i in range(40):
    # 날짜에 따른 종가 출력
    try:
        date = soup.find("td", attrs={'data-real-value':'{}'.format(time*86400 - (i*86400))})
        td_price = date.find_next_sibling("td")
        td_open = td_price.find_next_sibling("td")
        td_high = td_open.find_next_sibling("td")
        td_low = td_high.find_next_sibling("td")
        td_vol = td_low.find_next_sibling("td")
        td_change = td_vol .find_next_sibling("td")
        print(date.text+" "+td_price.text+" " + td_open.text + " " + td_high.text + " " + td_low.text + " "
              + td_vol.text + " " + td_change.text)
        #print(td_vol.text + " " + td_change.text)
        #print(date.text)
        #print(td_price.text)
        #print(td_open.text)
        #print(td_high.text)
        #print(td_low.text)
        #print(td_vol.text)
        #print(td_change.text)
    # 휴장 하는 날은 제외
    except:
        None

print("end")

# 추세를 표현할 수 있는 지수 EX) S&P / NASDAQ / KOSPI
# 10년 / 5년 / 1년 금리
# ++ 좀더 추가 가능
# 텐서 플로우 / CAFFE -> 예측 함수 추가 공부 필요
# 분류 / 군집 / 관계식
# 머신 러닝 -> 사람이 첫돌을 놔준다
# 딥러닝 -> 니가 알아서 해

