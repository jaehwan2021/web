import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}


url = "https://www.coupang.com/np/categories/497325"
res = requests.get(url, headers=headers)
res.raise_for_status()# 문제가 생기면 err 코드 내보내고 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^baby-product")})

print(items[0].find("div", attrs={"class":"name"}).get_text())
