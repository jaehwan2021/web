
import pymysql

conn = pymysql.connect(host='180.65.23.251', user='root', password='stockanalysis', db='pythondb', charset='utf8') ## 해당 db에 연결

try:
    cur = conn.cursor() ## 커서생성
    company_code = "apple" #table 이름 생성간 '-' 나 숫자 입력이 불가능함.. 일단 임시로 아무거나 적어둠


    sql = "CREATE TABLE IF NOT EXISTS " + company_code + "(date DATE, value FLOAT)" # 파일 생성
    cur.execute(sql) # 커서로sql 실행
    conn.commit() ## 저장

    sql = ""

finally: # database를 conn으로 연 후 항상 닫아주도록 finally 설정
    conn.close()

