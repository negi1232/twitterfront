import pymysql.cursors
import pymysql
import tweepy
import MySQLdb
import time
import datetime
# コネクションを作成します。
conn = pymysql.connect(

)

def friend_list_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "INSERT INTO friend_list (id_str,name,screen_name,location,description,url,protected,followers_count,friends_count,listed_count,created_at,favourites_count,profile_image_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur = conn.cursor()
    cur.executemany(insert_sql, values)

def follower_list_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "INSERT INTO follower_list (id_str,name,screen_name,location,description,url,protected,followers_count,friends_count,listed_count,created_at,favourites_count,profile_image_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

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

user = ""
#followerIDs = tweepy.Cursor(api.followers_ids, user).items()
#friendIDs=tweepy.Cursor(api.followers_ids, user).items()

#フレンドを取得
cur = conn.cursor()
cur.execute("DELETE  FROM friend_list")
cur.execute("ALTER TABLE bakusan.friend_list AUTO_INCREMENT=1")

friends_ids = []
my_info = api.me()
for friend_id in tweepy.Cursor(api.friends_ids, user_id=my_info.id).items():
    friends_ids.append(friend_id)

# 100IDsずつに詳細取得
values = list()
for i in range(0, len(friends_ids), 100):
    values=list()
    for data in api.lookup_users(user_ids=friends_ids[i:i+100]):
        
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
        
        values.append(st)

    friend_list_data_bulk(values)
    
#フォロワーを取得
cur = conn.cursor()
cur.execute("DELETE  FROM follower_list")
cur.execute("ALTER TABLE bakusan.follower_list AUTO_INCREMENT=1")
followers_ids = []
my_info = api.me()
for friend_id in tweepy.Cursor(api.followers_ids, user_id=my_info.id).items():
    followers_ids.append(friend_id)

# 100IDsずつに詳細取得
values = list()
for i in range(0, len(followers_ids), 100):
    values=list()
    for data in api.lookup_users(user_ids=followers_ids[i:i+100]):
        
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
        
        values.append(st)
        
    follower_list_data_bulk(values)

dt_now = datetime.datetime.now()
values=[datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),dt_now.year,dt_now.month,dt_now.day,len(followers_ids),len(friends_ids)]
insert_sql = "INSERT INTO account_stats (adddate,year,month,day,folower,follow) values (%s,%s,%s,%s,%s,%s)"
cur = conn.cursor()
cur.execute(insert_sql,values)

conn.commit()
conn.close()

