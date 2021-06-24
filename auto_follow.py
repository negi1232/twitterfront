import pymysql.cursors
import pymysql
import tweepy
import MySQLdb
import time
import time
import datetime
# コネクションを作成します。
conn = pymysql.connect(

)


CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_TOKEN        =
ACCESS_TOKEN_SECRET = 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

while(True):
    
    select_sql = 'select * from target_info WHERE flag IS NULL ORDER BY score DESC LIMIT 20'
    cur = conn.cursor()
    cur.execute(select_sql)
    result=cur.fetchall()
    for i in result:
        print(i[2])
        try :
            api.create_friendship(id=i[1])
            select_sql = "UPDATE target_info SET flag='done' where seq ="+str(i[0])
            select_sql2 = "UPDATE target_info SET add_date ='"+str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))+ "' where seq ="+str(i[0])
            cur = conn.cursor()
            cur.execute(select_sql)
            cur.execute(select_sql2)
            conn.commit()
        except:
            select_sql = "UPDATE target_info SET flag='undone' where seq ="+str(i[0])
            select_sql2 = "UPDATE target_info SET add_date ='"+str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))+ "' where seq ="+str(i[0])
            cur = conn.cursor()
            cur.execute(select_sql)
            cur.execute(select_sql2)
            conn.commit()
        
        time.sleep(300)