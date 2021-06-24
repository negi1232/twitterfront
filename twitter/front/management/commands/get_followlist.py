# -*- coding:utf-8 -*-
# followers.py

import tweepy
from django.core.management import BaseCommand
from ...models import AutoTweet
from ...models import AccountInfo
from django.utils import timezone
from django.utils.timezone import localtime 
import re
import datetime
import tweepy
from ...models import TargetList
import emoji
import re
import time
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        CONSUMER_KEY = "kCjXxFdP7VSeEkVFDkCHzhjxp"
        CONSUMER_SECRET = "H4MQLUH8ulLsRevNv7mikKWGknQ5MFmRF5rn8Lk3IYSgVsG9TU"
        ACCESS_TOKEN        = "1312805897270296578-Sfri0elOtOgOnL4Tg0h3d9XFqbbb4P"
        ACCESS_TOKEN_SECRET = "BPGlGWvSVqqYyHpdDVfOGNtA35sdg1z1Dnp0rEC6aPrKE"

        
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit = True)

        user = "hikakin"
        #followerIDs = tweepy.Cursor(api.followers_ids, user).items()

        followerDatas = []
        for article in TargetList.objects.all().filter(id_str=""):
            
            #print(article.followerid)
            print(article.seq)
            if len(TargetList.objects.filter(followerid=article.followerid))==1:#おなじID が存在しない場合
                try:
                    data = api.get_user(id =article.followerid)
                    #article.score=int(article.friends_count)/int(article.followers_count)
                    if data.name:
                        article.name=str(data.name.encode().decode("utf-8").encode("utf-8").decode("utf-8"))
                    if data.screen_name: 
                        article.screen_name=str(data.screen_name.encode().decode("utf-8").encode("utf-8").decode("utf-8"))
                    if data.location: 
                        article.location =data.location.encode().decode("utf-8").encode("utf-8").decode("utf-8")
                    if data.profile_location:
                        article.profile_location=data.profile_location.encode().decode("utf-8").encode("utf-8").decode("utf-8")
                    if data.description:
                        article.description=str(data.description.encode().decode("utf-8").encode("utf-8").decode("utf-8"))
                    if data.url :
                        article.url=data.url
                    if data.protected:
                        article.protected=data.protected
                    if data.followers_count:
                        article.followers_count=data.followers_count
                    if data.friends_count:
                        article.friends_count=data.friends_count
                    if data.listed_count:
                        article.listed_count=data.listed_count
                    if data.created_at:
                        article.created_at=data.created_at
                    if data.favourites_count:
                        article.favourites_count=data.favourites_count
                    if data.profile_image_url:
                        article.profile_image_url=data.profile_image_url

                    if int(article.friends_count)*int(article.followers_count)!=0:\
                        article.score=int(data.followers_count)/int(data.friends_count)
                    else:
                        article.score=0
                    
                    article.save()
                    
                except:
                    print("\/\/\/\/\/\eroor\/\/\/\/\/\/")
                    print(article.followerid)
                    article.delete()
                    print("\/\/\/\/\/\eroor\/\/\/\/\/\/")
            else:
                article=(TargetList.objects.filter(followerid=article.followerid))
                for i in range(1,len(article)+1):
                    print(article[i])
            
            time.sleep(0.5)

            
            
            
            
            #time.sleep(1)
    
    def remove_emoji(src_str):
        return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)