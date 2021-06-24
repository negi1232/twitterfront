# -*- coding:utf-8 -*-
# followers.py

import tweepy
from django.core.management import BaseCommand
from ...models import AutoTweet
from ...models import AccountStats
from django.utils import timezone
from django.utils.timezone import localtime 
import re
import datetime
import tweepy
from ...models import TargetList
import emoji
import re

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        CONSUMER_KEY = "kCjXxFdP7VSeEkVFDkCHzhjxp"
        CONSUMER_SECRET = "H4MQLUH8ulLsRevNv7mikKWGknQ5MFmRF5rn8Lk3IYSgVsG9TU"
        ACCESS_TOKEN        = "1312805897270296578-Sfri0elOtOgOnL4Tg0h3d9XFqbbb4P"
        ACCESS_TOKEN_SECRET = "BPGlGWvSVqqYyHpdDVfOGNtA35sdg1z1Dnp0rEC6aPrKE"


        
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit = True)

        user = "yousuck2020"
        followerIDs = tweepy.Cursor(api.followers_ids, user).items()
        for followerID in followerIDs:
            if len(TargetList.objects.filter(followerid=followerID))==0:
                article=TargetList()
                article.followerid=followerID
                article.save()
                print(followerID)
            else:
                print(TargetList.objects.filter(followerid=followerID))
                
