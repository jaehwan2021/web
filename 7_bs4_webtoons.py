import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()# 문제가 생기면 err 코드 내보내고 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.get_text())





