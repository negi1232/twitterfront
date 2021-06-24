import pymysql.cursors
import pymysql
import tweepy
import MySQLdb
import time
# コネクションを作成します。
conn = pymysql.connect(

)

def insert_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "INSERT INTO target_list (followerID) values (%s)"

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
user = "ariyoshihiroiki"
followerIDs = tweepy.Cursor(api.followers_ids, user).items()
#print("5")
i=0
values = []
for IDs in followerIDs:
    #print(IDs)
    values.append(IDs)
    #print((1+len(values))%1000)
    if (1+len(values))%5000==0:
        print((1+len(values)))
        insert_data_bulk(values)
        
        values=[]
        conn.commit()
        time.sleep(60)

c.close()
print(values)


