import pymysql.cursors
import pymysql
import tweepy
import MySQLdb
import time
conn = pymysql.connect(

)

def insert_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "INSERT INTO target_info (id_str,name,screen_name,location,profile_location,description,url,protected,followers_count,friends_count,listed_count,created_at,favourites_count,profile_image_url,score) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur = conn.cursor()
    cur.executemany(insert_sql, values)

def uodata_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "UPDATE target_info  SET get_flag=done where seq = %s"

    cur = conn.cursor()
    cur.executemany(insert_sql, values)

#print("1")
CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_TOKEN        = 
ACCESS_TOKEN_SECRET = 
#print("2")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#print("3")
api = tweepy.API(auth,wait_on_rate_limit = True)
#print("4")
values = list()
dones=list()
select_sql = 'select * from target_list WHERE get_flag IS NULL LIMIT 100'


while(True):
    cur = conn.cursor()
    cur.execute(select_sql)
    result=cur.fetchall()
    for i in range(len(result)):
        print(result[i][0],result[i][1])
        try:
            data = api.get_user(id =result[i][1])
        
            st=list()
            if data.id_str:
                st.append(data.id_str)
            else:
                st.append("")
            if data.name:
                st.append(str(data.name).encode().decode("utf-8").encode("utf-8").decode("utf-8"))
            else:
                st.append("")
            if data.screen_name: 
                st.append(str(data.screen_name).encode().decode("utf-8").encode("utf-8").decode("utf-8"))
            else:
                st.append("")
            if data.location: 
                st.append(str(data.location).encode().decode("utf-8").encode("utf-8").decode("utf-8"))
            else:
                st.append("")
            if data.profile_location:
                st.append(str(data.profile_location).encode().decode("utf-8").encode("utf-8").decode("utf-8"))
            else:
                st.append("")
            if data.description:
                st.append(str(data.description).encode().decode("utf-8").encode("utf-8").decode("utf-8"))
            else:
                st.append("")
            if data.url :
                st.append(data.url)
            else:
                st.append("")
            if data.protected:
                st.append(data.protected)
            else:
                st.append("")
            if data.followers_count:
                st.append(data.followers_count)
            else:
                st.append(0)
            if data.friends_count:
                st.append(data.friends_count)
            else:
                st.append(0)
            if data.listed_count:
                st.append(data.listed_count)
            else:
                st.append(0)
            if data.created_at:
                st.append(data.created_at)
            else:
                st.append("")
            if data.favourites_count:
                st.append(data.favourites_count)
            else:
                st.append(0)
            if data.profile_image_url:
                st.append(data.profile_image_url)
            else:
                st.append("")

            if int(data.friends_count)*int(data.followers_count)!=0 and data.protected==0 :
                st.append(int(data.friends_count)/int(data.followers_count))
            else:
                st.append(0)
            values.append(st)

            cur = conn.cursor()
            cur.execute("UPDATE target_list  SET get_flag='done' where seq ="+str(result[i][0]))
        
        except:
            cur = conn.cursor()
            cur.execute("UPDATE target_list  SET get_flag='undone' where seq ="+str(result[i][0]))

        time.sleep(1)
        #print((1+len(values))%51)
        if (1+len(values))%51==0:
            print((1+len(values)))
            insert_data_bulk(values)
            values=[]
            conn.commit()
        if i==99:#0~99
            print((1+len(values)))
            insert_data_bulk(values)
            values=[]
            conn.commit()
            break

conn.close()


