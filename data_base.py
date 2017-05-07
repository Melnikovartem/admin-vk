import sqlite3
import config
from time import strftime

def new_write(online):
    con = sqlite3.connect(config.database)
    cur = con.cursor()
    put_into = []
    online_add =" "
    for i in online:
        online_add+="</Art_*"+i['last_name']+" "+i['first_name']+"<.>Mel/"+str(i['uid'])
    print(online)
    print(online_add)
    put_into.append(strftime('%H:%M:%S %D'))
    put_into.append(online_add)
    put_into.append(0)
    
    cur.execute("insert into "+ config.post_table +" values (?,?,?);", put_into)

    con.commit()
    con.close()

def update_inf():
    pass


def get_inf():
    
    pass
