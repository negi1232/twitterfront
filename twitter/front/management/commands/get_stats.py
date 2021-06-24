from django.core.management import BaseCommand
from ...models import FollowList
from ...models import TargetList
from ...models import AccountStats
from django.utils import timezone
from django.utils.timezone import localtime 
import re
import tweepy
import datetime
import time
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **options):
        CONSUMER_KEY = "kCjXxFdP7VSeEkVFDkCHzhjxp"
        CONSUMER_SECRET = "H4MQLUH8ulLsRevNv7mikKWGknQ5MFmRF5rn8Lk3IYSgVsG9TU"
        ACCESS_TOKEN        = "1312805897270296578-Sfri0elOtOgOnL4Tg0h3d9XFqbbb4P"
        ACCESS_TOKEN_SECRET = "BPGlGWvSVqqYyHpdDVfOGNtA35sdg1z1Dnp0rEC6aPrKE"

        
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit = True)

        user = "30jf5CNGKHmLITu"
        #followerIDs = tweepy.Cursor(api.followers_ids, user).items()
        #friendIDs=tweepy.Cursor(api.followers_ids, user).items()
        friends = []
        for friend in tweepy.Cursor(api.friends_ids).items():
            friends.append(friend)

        followers = []
        for follower in tweepy.Cursor(api.followers_ids).items():
            followers.append(friend)


        article=AccountStats()
        article.folower=len(followers)
        article.follow=len(friends)

        dt_now = datetime.datetime.now()
        article.year=dt_now.year
        article.month=dt_now.month
        article.day=dt_now.day
        article.adddate=timezone.now().strftime('%Y-%m-%dT%H:%M:%S')

        article.save()

