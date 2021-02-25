

import pymysql


def save(file_name):

    list_Data_value = [1, 2, 3, 4] #
    list_Data_date = [5, 6, 7, 8]

    conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='pythondb',
                           charset='utf8')  ## 해당 db에 연결

    try:
        cur = conn.cursor()  ## 커서생성
        company_code = file_name  # table 이름 생성간 '-' 나 숫자 입력이 불가능함.. 일단 임시로 아무거나 적어둠
        sql = "CREATE TABLE IF NOT EXISTS " + company_code + "(date INT, value INT)"  # 파일 생성
        cur.execute(sql)  # 커서로sql 실행

        for i in range(3):

            sql = "insert into " + company_code + "(date, value) values (%s, %s)"
            cur.execute(sql, (list_Data_date[i], list_Data_value[i]))


        conn.commit()  ## 저장

    finally:  # database를 conn으로 연 후 항상 닫아주도록 finally 설정
        conn.close()

save("deve")

# 마리아db - python 연동후 data 입력 code https://reddb.tistory.com/139 참고해서 HeidiSQL 다운받아 확인가능
# 호스트명/IP 180.65.23.251 사용자 root 암호 stockanalysis
#
# conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='pythonDB', charset='utf8') ## 해당 db에 연결 접속정보
#
# try:
#     cur = conn.cursor() ## 커서생성
#     data1 = input("사용자 ID를 입력하세요(엔터 클릭 시 종료): ") # data1변수에 ID 입력받기
#     data2 = input("사용자 이름을 입력하세요: ")
#     data3 = input("사용자 이메일을 입력하세요: ")
#     data4 = input("사용자 출생연도를 입력하세요: ")
#     sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")" # sql변수에 INSERT SQL문 입력
#     cur.execute(sql) # 커서로sql 실행
#     conn.commit() ## 저장
#
# finally: # database를 conn으로 연 후 항상 닫아주도록 finally 설정
#     conn.close()
