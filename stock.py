# from selenium import webdriver
#
# chrome_driver = webdriver.Chrome('C:\\Users\\82109\\Desktop\\chromedriver_win32\\chromedriver.exe')
#
# chrome_driver.implicitly_wait(5)
#
# chrome_driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
#
# chrome_driver.find_element_by_id('gjhh1588').send_keys('naver')
#
# chrome_driver.find_element_by_id('rla1082016!@').send_keys('naver')
#
# chrome_driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# from selenium import webdriver
# import time
#
# driver = webdriver.PhantomJS('C:\\Users\\82109\\Desktop\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(3)
# print(driver.find_element_by_id("content").text)
# driver.close()
#
# import numpy as np
#
# print(np.matrix([ [ 1, 2 ], [ 2, 3 ]]))
#
#
#
# '''
# c = close
# h = high
# l = low
# o = open
# '''

import pymysql
### data 입력하기
conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='testdb', charset='utf8') # testdb database에 연결

try:
    curs = conn.cursor()
    sql = """insert into mysql_test(id, name, region)
            values (%s, %s, %s)"""
    ## 수정시 """update mysql_test set region='서울특별시' where region='서울'"""
    # curs.execute(sql)
    ## 삭제시 """delete fron mysql_test where region=%s"""
    # curs.execute(sql, '부산')

    curs.execute(sql, ('test10', '테스트10', '천안'))
    curs.execute(sql, ('test11', '테스트10', '아산'))
    conn.commit() # data가 db에 저장됨

    sql2 = "select * from mysql_test order by no"
    curs.execute(sql2)
    rows = curs.fetchall()
    print(rows)
finally: # database를 conn으로 연 후 항상 닫아주도록 finally 설정
    conn.close()

exit() ## conn을 종료

# ### data 가져오기
# conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='testdb', charset='utf8') # testdb database에 연결
# curs = conn.cursor(pymysql.cursors.DictCursor) # 커서 가져오기 # 안에 있는건 dictcursor은 row['no'] 형태의 data table내 열 값을 통한 data 불러오기를 가능하게함
# sql = "select * from mysql_test where region=%s" # 실행할 명령 입력(query문) # where 부터는 조건문 %s는 이후 실행문에서 조건을 추가하기 위한 변수
# curs.execute(sql, '서울') # 실행문 # 뒤에 오는 서울은 %s에 들어가게됨
#
# rows = curs.fetchall() #fetchall 레코드를 모두 가져옴 / fetchmany 지정한 갯수만큼 / fetchone 1개의 레코드만 가져옴
#
# for row in rows: # 특정 값만 가져오기 위한 for문
#     print(row)
#     print(row['no'], row['id'], row['name'])
#
# conn.close()