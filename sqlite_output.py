import os,sqlite3

class Sqlite_Outputer(object):
    def __init__(self):
        self.datas = []
	
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_db(self,db_name):
        person_table = {}
        relation_table = []

        print('Prepare data for database insert.')
        for data in self.datas:
            #person #name,number_of friends,img_src
            name = data['name']
            del data['name']

            #person_table[name]['name'] = name
            if name not in person_table:
                person_table[name]={'nof':len(data),'img':'NULL'}
            else:
                person_table[name]['nof'] = len(data)

            for friend in data.values():
                fname = friend['friend_name']
                fimg = friend['friend_img']
                frelation = friend['friend_relationship']
                #person
                if fname not in person_table:
                    person_table[fname]={'nof':'NULL','img':fimg}
                else:
                    person_table[fname]['img'] = fimg
                #relation
                relation_table.append({'p_name':name,'f_name':fname,'relation':frelation})

        #connect db
        print('Connecting database.')
        db_file = os.path.join(os.path.dirname(__file__),db_name)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        print('Database insert start.')
        count = 0
        for name,values in person_table.items():
            count+=1
            cursor.execute(r'insert into celebrity values (?,?,?,?)',(count,name,values['nof'],values['img']))


        count = 0
        for r in relation_table:
            count+=1
            cursor.execute(r'insert into relationship values (?,?,?,?)',(count,r['p_name'],r['f_name'],r['relation']))
        cursor.close()
        conn.commit()
        conn.close()
        print('Database insert complete.')
        
