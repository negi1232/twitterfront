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


class Command(BaseCommand):

    def handle(self, *args, **options):
        for article in TargetList.objects.all():
            
            if bool(article.id_str)==True:
                
                if int(article.friends_count)*int(article.followers_count)!=0:
                    # print(int(article.friends_count)/int(article.followers_count))
                    # print("//////////////////")
                    article.score=int(article.followers_count)/int(article.friends_count)
                else:
                    article.score=0
                article.save()
            
            
           
    
    def remove_emoji(src_str):
        return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)