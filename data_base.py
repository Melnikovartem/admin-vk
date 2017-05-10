import sqlite3
import config
from time import strftime

def new_write(online):
    con = sqlite3.connect(config.database)
    cur = con.cursor()
    put_into = []
    online_add =""
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

    update_inf()

    return 0

def update_inf():
    
    con = sqlite3.connect(config.database)
    cur = con.cursor()

    cur.execute("select * from "+ config.post_table +" WHERE Update_status = 0")
    ans = cur.fetchall()
    
    cur.execute("select * from "+ config.users_table)
    now = cur.fetchall()

    now_dic = {}
    id_list = []
    for i in now:
        now_dic[i[0]] = [i[1], i[2]]
        id_list.append(i[0])

    added = id_list[:]
    for i in ans:
        inf1 = i[1].split("</Art_*")
        for j in inf1:
            
            if not(j == ""):
                inf = j.split("<.>Mel/")
                inf[1] = int(inf[1])
                if not(now_dic.get(inf[1])):
                    now_dic[inf[1]]=[inf[0], 0]
                    if added.count(inf[1]) == 0:
                        added.append(inf[1])
                now_dic[inf[1]][1] += 1
    for i in added:
        if id_list.count(i) > 0:
            cur.execute("UPDATE "+ config.users_table +" SET Number = " + str(now_dic[i][1]) +  " WHERE Id = " + str(i))
        else:
            put_into = [i,now_dic[i][0] ,now_dic[i][1]]
            cur.execute("insert into "+ config.users_table +" values (?,?,?);", put_into)
    cur.execute("UPDATE "+ config.post_table +" SET Update_status = 1 WHERE Update_status = 0")

    con.commit()
    con.close()

    return 0

def get_inf():
    con = sqlite3.connect(config.database)
    cur = con.cursor()

    cur.execute("select * from "+ config.post_table)
    _all = cur.fetchall()

    if _all == 0:
        _all = 1
    
    cur.execute("select * from "+ config.users_table)
    now = cur.fetchall()
    
    con.close()

    ans = []
    for i in now:
        proc = str(round(100*i[2]/len(_all)))
        ans.append({"href":"https://vk.com/id" + str(i[0]),"proc_need": "width: " + proc + "%;","name":i[1], "proc": proc + "%"})
    return ans
