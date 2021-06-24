from django.core.management import BaseCommand
from ...models import AutoTweet
from ...models import AccountInfo
from django.utils import timezone
from django.utils.timezone import localtime 
import re
import datetime
class Command(BaseCommand):

    def handle(self, *args, **options):
        now_time=localtime(timezone.now()).strftime('%Y-%m-%dT%H:%M')#タイムゾーンを日本に設定
        print("////////////////////")
        now_time=re.split('(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', now_time)
        for i in range(1,6):
            now_time[i]=int(now_time[i])
        
        dt1=datetime.datetime(now_time[1],now_time[2],now_time[3],now_time[4],now_time[5])
        print("現在時刻-",end=":")
        print(dt1)
        
        articles = AutoTweet.objects.order_by('reserve_date').filter(tw_flg='0')#もっとも近い時間に投稿予定のオブジェクトを検索

        article=articles[0]
        
        reserve_time=re.split('(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', article.reserve_date)
        
        for i in range(1,6):
            reserve_time[i]=int(reserve_time[i])

        dt2=datetime.datetime(reserve_time[1],reserve_time[2],reserve_time[3],reserve_time[4],reserve_time[5])
        print("予約時刻-",end=":")
        print(dt2)
        #投稿時間に達しているかを判断
        difsecond=(dt1-dt2)#1以上であればスルー 0以下であればツイート　
        print(difsecond)
        print(difsecond.total_seconds())

        if difsecond.total_seconds()>=0:
            print("Tweet")
            print("////////////////////")
            articleprint(article)
            #tweetが完了した場合
            article.tw_flg=1#tweetが完了
            #print(accountarticles[0].disp_name)
            article.updated=str(timezone.now().strftime('%Y-%m-%dT%H:%M'))#投稿時刻を記録
            article.save()
            #AccountInfoについて記載
            accountarticles=AccountInfo.objects.filter(kanriid="2006")
            accountarticle=accountarticles[0]
            
            accountarticle.latest_tweet=str(timezone.now().strftime('%Y-%m-%dT%H:%M'))
            accountarticle.latest_tweet_seq=article.seq

            accountarticle.save()
            return 0
        elif difsecond.total_seconds()<0:
            print("Not Tweet")
            return 0
        


def articleprint(article):
    print(article.seq)
    print(article.tweet)
    print(article.img_path1)
    print(article.img_path2)
    print(article.img_path3)
    print(article.img_path4)
