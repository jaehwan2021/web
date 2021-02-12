#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    collect_global_stock_in_investing.py
"""
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import numpy as np

def arrayToNumeric(a):
    nums = []
    for i in range(0,len(a)):
        nums.append(re.sub(r'[a-zA-Z%]', r'', a[i].text))
    return nums
### a로 받은 무언가(주소 같음)를 리스트 형태의 숫자로 반환함

def get_stock_info_investing(country_num, page_num):
    """
    :param country_num: 국가번호 investing.com에서 사용
    :return: 종목 url, 종목명, 종목코드(로컬코드) 테이블
    """
    driver = webdriver.PhantomJS()
    stock_info = []

    url = "https://www.investing.com/stock-screener/?sp=country::" + str(country_num) +"|sector::a|industry::a|equityType::a<eq_market_cap;" + str(page_num) +""
    driver.get(url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultsTable")))
    html_text = driver.page_source
    soup = bs(html_text, 'lxml')
    ref_tags = soup.find_all(href=True, title=True)

    for ref_tag in ref_tags:
        if "/equities/" in ref_tag['href']:
            stock_url = ref_tag['href'].replace("/equities/","")
            name = ref_tag.text
            d = soup.find(text=name)
            symbol = d.find_next("td").text
            stock_info.append([stock_url,name,symbol])

    return(np.array(stock_info))

def write_to_csvfile(filename, array_data):
    csv_file = open(filename, "w",newline='')
    cw = csv.writer(csv_file , delimiter=',', quotechar='|')
    for row in array_data:
        cw.writerow(row)

    csv_file.close()

def read_from_csvfile(filename):

    csv_file = open(filename, "r",newline='')
    cr = csv.reader(csv_file , delimiter=',', quotechar='|')
    data=[]
    for row in cr:
        data.append(row)

    csv_file.close()
    return data

def batch_save_country_stock_info(country_num):
    """

    국가의 종목코드와 종목 url이 포함되어 있는 .CSV 파일을 만든다.
    종목 URL은 INVETING.COM에서
    """
    stock_info = get_stock_info_investing(country_num, 1)

    if len(stock_info)>=50:
        for page_num in range(2,300):
            new_stock_info = get_stock_info_investing(country_num, page_num)
            stock_info = np.concatenate((stock_info,new_stock_info), axis=0)
            print(str(page_num) + " Loading success!")
            #종목 숫자가 50개 이하이면
            if len(new_stock_info)<50:
                print("Done!")
                break

    write_to_csvfile("stock"+ str(country_num)+ ".csv", stock_info)

################## 종목 코드 수집 과정

def get_fs_soup_object_from_inveting(company_url,freq="a",fs_type="BS"):
    """
    재무상태표, 손익계산서, 현금흐름표 계정에 있는 데이터를 가져온다.
    fs_type : BS, IS, CF

    return : soup 객체를 반환한다.
    """
    fs_dict = {'BS': 'balance-sheet', 'IS': 'income-statement', 'CF': 'cash-flow'}

    url = "https://www.investing.com/equities/" + company_url + "-" + fs_dict[fs_type]
    driver = webdriver.PhantomJS()
    driver.get(url)

    if freq=="a":
        driver.find_element_by_css_selector("a.newBtn.toggleButton.LightGray").click()
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'header_row')))

    html_text = driver.page_source
    soup = bs(html_text, 'lxml')

    return soup

def get_fs_data_from_soup(soup,item, n=1):

    """
    soup 객체에서 item을 찾아서 반환해준다.
    """
    results = []
    try:
        d = soup.find_all(text=item)
        d_ = d[0].find_all_next("td", limit=n)
        for r in d_:
            results.append(r.text)
    except:
        print("error")
        return None
    return results

# 예제 : 엔비디아의 정보 가져오기

company_url = "nvidia-corp"
is_soup = get_fs_soup_object_from_inveting(company_url,'a',"IS")
bs_soup = get_fs_soup_object_from_inveting(company_url,'a',"BS")
cf_soup = get_fs_soup_object_from_inveting(company_url,'a',"CF")

get_fs_data_from_soup(is_soup,"Operating Income",4)
get_fs_data_from_soup(bs_soup,"Total Inventory",4)
get_fs_data_from_soup(cf_soup,"Cash From Operating Activities",4)