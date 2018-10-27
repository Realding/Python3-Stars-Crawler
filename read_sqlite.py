import os,sqlite3,sys

db_name = 'test.db'
db_file = os.path.join(os.path.dirname(__file__),db_name)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
try:
    count =0
    while True:
        count+=1
        line=sys.stdin.readline()
        cursor.execute(line)
        values = cursor.fetchall()
        print(values)
        if not line:
            break
        print(count,line)
finally:
    cursor.close()
    conn.close()
