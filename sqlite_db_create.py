import os,sqlite3

def dbcreate(db_name):
    db_file = os.path.join(os.path.dirname(__file__),db_name)

    if os.path.isfile(db_file):
        os.remove(db_file)
        print("db file removed.")

    #initialization
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    #stars table
    cursor.execute('create table celebrity (id int primary key,name varchar(20),number_of_friends int,img_src varchar(200))')
    #relation table
    cursor.execute('create table relationship ( id int primary key,\
                                            p_name varchar(20),\
                                            f_name varchar(20),\
                                            relation varchar(20)\
                                            )')
    '''
    foreign key (p_name) references celebrity(name),\
    foreign key (f_name) references celebrity(name)\
    '''
    cursor.close()
    conn.commit()
    conn.close()
