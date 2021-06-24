from django.core.management import BaseCommand
from ...models import FollowList
from ...models import TargetList
from ...models import AccountInfo
from django.utils import timezone
from django.utils.timezone import localtime 
import re
import tweepy
import datetime
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

        articles =  TargetList.objects.order_by('-score').filter(protected='False').filter(flag=0)
        #articles=articles.filter(flag)
        for i in articles:
            print(i.screen_name)
            api.create_friendship(screen_name=str(i.screen_name))
            i.flag=1
            i.save()
            time.sleep(300)

