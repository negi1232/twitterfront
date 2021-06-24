from django.db import models

# class TweetArticle(models.Model):
#     content = models.CharField(max_length=280)
#     posting_time = models.DateTimeField(max_length=200, null = True)
#     image1= models.ImageField(upload_to='documents/',blank=True, null=True,default='')
#     image2= models.ImageField(upload_to='documents/',blank=True, null=True,default='')
#     image3= models.ImageField(upload_to='documents/',blank=True, null=True,default='')
#     image4= models.ImageField(upload_to='documents/',blank=True, null=True,default='')
#     def __str__(self):
#         return self.content


class AutoTweet(models.Model):
    seq = models.AutoField(primary_key=True)
    kanriid = models.CharField(max_length=5)
    tweet = models.CharField(max_length=280)
    tw_flg = models.CharField(max_length=1)
    updated = models.CharField(max_length=20)
    reserve_date = models.CharField(max_length=16)
    img_path1 = models.ImageField(upload_to='documents/',blank=True, null=True,default='')
    img_path2 = models.ImageField(upload_to='documents/',blank=True, null=True,default='')
    img_path3 = models.ImageField(upload_to='documents/',blank=True, null=True,default='')
    img_path4 = models.ImageField(upload_to='documents/',blank=True, null=True,default='')
    tweet_url = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    info_url = models.CharField(max_length=200, blank=True, null=True)
    tweet_id = models.CharField(max_length=30, blank=True, null=True)
    gif_path = models.CharField(max_length=200, blank=True, null=True)
    touhyou = models.CharField(max_length=30, blank=True, null=True)
    emoji = models.CharField(max_length=30, blank=True, null=True)
    hashtag = models.CharField(max_length=30, blank=True, null=True)
    flag = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'auto_tweet'

class FollowList(models.Model):
    seq = models.AutoField(primary_key=True)
    kanriid = models.CharField(max_length=5)
    guid = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=50)
    score = models.CharField(max_length=4)
    follow_date = models.CharField(max_length=16)
    add_date = models.CharField(max_length=16)
    follow_flag = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'follow_list'

class AccountInfo(models.Model):
    kanriid = models.CharField(primary_key=True, max_length=50)
    disp_name = models.CharField(max_length=50)
    url = models.CharField(db_column='URL', max_length=100)  # Field name made lowercase.
    latest_tweet = models.CharField(max_length=16)
    latest_tweet_seq = models.IntegerField()
    latest_tweet_url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ACCOUNT_INFO'
        
# class TargetList(models.Model):
#     seq = models.AutoField(primary_key=True)
#     id_str = models.CharField(max_length=20, blank=True, null=True)
#     name = models.CharField(max_length=1000, blank=True, null=True)
#     screen_name = models.CharField(max_length=100, blank=True, null=True)
#     location = models.CharField(max_length=300, blank=True, null=True)
#     profile_location = models.CharField(max_length=300, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     url = models.CharField(max_length=100, blank=True, null=True)
#     protected = models.CharField(max_length=10, blank=True, null=True)
#     followers_count = models.CharField(max_length=15, blank=True, null=True)
#     friends_count = models.CharField(max_length=15, blank=True, null=True)
#     listed_count = models.CharField(max_length=10, blank=True, null=True)
#     created_at = models.CharField(max_length=100, blank=True, null=True)
#     favourites_count = models.CharField(max_length=20, blank=True, null=True)
#     profile_image_url = models.CharField(max_length=100, blank=True, null=True)
#     followerid = models.CharField(db_column='followerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     score = models.FloatField(blank=True, null=True)
#     flag = models.CharField(max_length=1, blank=True, null=True)
#     followdate = models.CharField(max_length=16, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'target_list'

class TargetInfo(models.Model):
    seq = models.AutoField(primary_key=True)
    id_str = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100)
    location = models.CharField(max_length=500, blank=True, null=True)
    profile_location = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=750, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    protected = models.CharField(max_length=100)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    listed_count = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=100, blank=True, null=True)
    favourites_count = models.IntegerField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=500, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    flag = models.CharField(max_length=100, blank=True, null=True)
    add_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'target_info'

class AccountStats(models.Model):
    month = models.CharField(max_length=5, blank=True, null=True)
    day = models.CharField(max_length=5, blank=True, null=True)
    folower = models.CharField(max_length=100, blank=True, null=True)
    follow = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    seq = models.AutoField(primary_key=True)
    adddate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_stats'