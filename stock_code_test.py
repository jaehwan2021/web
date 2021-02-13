
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime


url = 'https://www.investing.com/equities/jp-morgan-chase-historical-data'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}
req = requests.get(url, headers=headers)
req.raise_for_status()
soup = BeautifulSoup(req.text, 'lxml')

time = input()

#18667 = 2월 9일

date = soup.find("td", attrs={'data-real-value':'{}'.format(time)})
price = date.find_next_sibling("td")

print(date.text)
print(price.text)






#dsf