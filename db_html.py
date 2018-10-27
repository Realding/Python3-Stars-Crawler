#db_html
import os,sqlite3

db_name = 'test.db'
db_file = os.path.join(os.path.dirname(__file__),db_name)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
try:
    fout = open("output.html","w",encoding="utf-8")
    sqlquery1 = r"select * from celebrity"
    cursor.execute(sqlquery1)
    lines = cursor.fetchall()
    fout.write("\
    <!DOCTYPE html>\n\
    <html>\n\
    <head>\n\
            <meta http-equiv='content-type' content='text/html;charset=\'utf-8\'>\n\
            <title>Stars</title>\n\
    </head>\n\
    <body>\n\
    <table border = '1'>\n\
    ")
    count=0
    for line in lines:
        if(count%4==0):
            fout.write("<tr>")
        fout.write("<td>{0}</td><td>{1}</td><td><img src=\"{2}\" width=\"100\" height=\"100\"></td>\n".format(line[0],line[1],line[3]))
        if(count%4==3):
            fout.write("</tr>")
        count+=1
    fout.write("\
    </table>\n\
    </body>\n\
    </html>\
    ")
    
        
finally:
    fout.close()
    cursor.close()
    conn.close()
