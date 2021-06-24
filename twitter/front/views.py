# -*- coding: utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import ReservationTweetForm
from .forms import SearchForm
from .forms import AddFollow
from .frontdef import datadifference
# from .models import TweetArticle
from .models import AutoTweet
from .models import FollowList
#from .models import TargetList
from .models import TargetInfo
from django.utils import timezone
import datetime
import schedule
import time
import sys
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import tweepy
def job():
  #print(datetime.datetime.now())
  print("I'm working...")  

# Create your views here.
def index(request):

    return render(request, 'front/index.html')

def toppage(request):
    context = {
        'todayfollow': 10,
        'follow': 100,
        'todayfollower': 20,
        'follower': 200,
    }
    
    return render(request, 'front/toppage.html',context)

def getfollowtargetstats(id):
    CONSUMER_KEY = 
    CONSUMER_SECRET = 
    ACCESS_TOKEN        =
    ACCESS_TOKEN_SECRET = 

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit = True)
    print(id)
    print(len(TargetInfo.objects.filter(screen_name=id)))
    if len(TargetInfo.objects.filter(screen_name=id))==0:
        try:
            
            article=TargetInfo()
            data = api.get_user(screen_name =id)
            if data.id_str:
                article.id_str=data.id_str
            else:
                article.id_str=""
            if data.name:
                article.name=str(data.name).encode().decode("utf-8").encode("utf-8").decode("utf-8")
            else:
                article.name=""
            if data.screen_name: 
                article.screen_name=str(data.screen_name).encode().decode("utf-8").encode("utf-8").decode("utf-8")
            else:
                article.screen_name=""
            if data.location: 
                article.location =str(data.location).encode().decode("utf-8").encode("utf-8").decode("utf-8")
            else:
                article.location=""
            if data.profile_location:
                article.profile_location=str(data.profile_location).encode().decode("utf-8").encode("utf-8").decode("utf-8")
            else:
                article.profile_location=""
            if data.description:
                article.description=str(data.description).encode().decode("utf-8").encode("utf-8").decode("utf-8")
            else:
                article.description=""
            if data.url :
                article.url=data.url
            else:
                article.url=""
            if data.protected:
                article.protected=data.protected
            else:
                article.protected=""
            if data.followers_count:
                article.followers_count=data.followers_count
            else:
                article.followers_count=""
            if data.friends_count:
                article.friends_count=data.friends_count
            else:
                article.friends_count=""
            if data.listed_count:
                article.listed_count=data.listed_count
            else:
                article.listed_count=""
            if data.created_at:
                article.created_at=data.created_at
            else:
                article.created_at=""
            if data.favourites_count:
                article.favourites_count=data.favourites_count
            else:
                article.favourites_count=""
            if data.profile_image_url:
                article.profile_image_url=data.profile_image_url
            else:
                article.profile_image_url=""
            
            article.score="9999"
            article.save()
            return "Done"
            
        except:
            return "ERROR"
    else:
        article=TargetInfo.objects.filter(screen_name=id)
        for i in article:
            i.score="9999"
            i.save()
        return "Done2"



def priorityfollow(request):#優先的にフォローするアカウントを追加する
    #params = {'Follow': ''}
    if 'pageNo' in request.GET:
        pageNo = request.GET['pageNo']
    else :
        pageNo=1
    
    
    if request.method == 'POST':
        res=str()
        res =  getfollowtargetstats(request.POST['Follow'])
        

        articles = TargetInfo.objects.order_by('-score').filter(flag__isnull=True)
        paginator  = Paginator(articles, 20)
        articles = paginator.get_page(int(pageNo)) 
        params={
            'result':res,
            'form':AddFollow(),
            'articles':articles,
            'pageNo':pageNo,
           
        }
        return render(request, 'front/priorityfollow.html', params)
    else:#GETの場合
        articles = TargetInfo.objects.order_by('-score').filter(flag__isnull=True)
        paginator  = Paginator(articles, 20)
        articles = paginator.get_page(int(pageNo)) 
        params={
            'form':AddFollow(),
            'articles':articles,
            'pageNo':pageNo,
        }
        return render(request, 'front/priorityfollow.html', params)

def followlistdel(request, id):
    TargetInfo.objects.filter(seq=id)
    print(TargetInfo.objects.filter(seq=id))
    for i in TargetInfo.objects.filter(seq=id):
        i.score="-2"
        i.save()
    params={
            'form':AddFollow(),
            'articles':TargetInfo.objects.order_by('-score').filter(flag__isnull=True)[:100]
        }
    return render(request, 'front/priorityfollow.html', params)

def follow_list(request):
    #params = {'Follow': ''}

    if 'pageNo' in request.GET:
        pageNo = request.GET['pageNo']
    else :
        pageNo=1
    articles = TargetInfo.objects.order_by('-add_date').filter(flag='done')[:100]
    paginator  = Paginator(articles, 20)
    articles = paginator.get_page(int(pageNo)) 
    
    params={
        'articles':articles,
        'pageNo':pageNo,
    }
    return render(request, 'front/follow_list.html', params)


def autotweet(request):#ツイートの予約投稿
    params = {'contents': '', 'tweet_time': 'image', 'form': None}
    if request.method == 'POST':
        #print(request.POST['content'])

        imagelist=request.FILES.getlist("image")
        

        article = AutoTweet(tweet=request.POST['content'],
                                reserve_date=request.POST['posting_time'],
                                tw_flg=0
        )

        images=len(imagelist)
        print(images)
        if images>=1:
            article.img_path1=imagelist[0]
        if images>=2:
            article.img_path2=imagelist[1]
        if images>=3:
            article.img_path3=imagelist[2]
        if images>=4:
            article.img_path4=imagelist[3]



        article.save()
        return HttpResponseRedirect("/front/posttweetview")
        #return render(request, 'front/index.html')
    else:#GETの場合
        params['form'] = ReservationTweetForm()
        return render(request, 'front/autotweet.html', params)


def posttweetview(request):#予約投稿の一覧
    #articles = Article.objects.all()
    
    if 'pageNo' in request.GET:
        pageNo = request.GET['pageNo']
    else :
        pageNo=1

    articles = AutoTweet.objects.order_by('reserve_date').filter(tw_flg='0')
    paginator  = Paginator(articles, 20)
    articles = paginator.get_page(int(pageNo))
    # print("/////////////////////")
    # print(articles)
    # print("/////////////////////")
    context={
        'articles':articles,
        'massage':"予約投稿一覧",
        'searchform':SearchForm,
        'pageNo':pageNo,
    }
    #for i in articles:
    #    print(i.reserve_date)

    

    return render(request, 'front/index.html',context)

def tweetview(request):#投稿の一覧
    #articles = Article.objects.all()
    articles = AutoTweet.objects.order_by('-reserve_date').filter(tw_flg='1')
    print("/////////////////////")
    print(articles)
    print("/////////////////////")
    context={
        'articles':articles,
        'massage':"投稿一覧"
    }
    #for i in articles:
    #    print(i.reserve_date)

    

    return render(request, 'front/index.html',context)

def detail(request, id):
    article = get_object_or_404(AutoTweet, pk=id)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'front/detail.html', context)

def accountdetail(request, id):
    article = get_object_or_404(TargetInfo, pk=id)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'front/accountdetail.html', context)

def edit(request, id):
    article = get_object_or_404(AutoTweet,seq=id)
    print("////////////////////")
    print(article.img_path1)
    print("////////////////////")
    form = ReservationTweetForm(initial={'seq':article.seq,
    'kanriid':article.kanriid,
    'content':article.tweet,
    'posting_time':article.reserve_date,
    'image_1':article.img_path1,
    'image_2':article.img_path2,
    'image_3':article.img_path3,
    'image_4':article.img_path4,
        })
    print("////////////////////")
    print("////////////////////")
    context = {
        'message': 'Edit Article',
        'article': article,
        'form': form,
    }
    return render(request, 'front/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        
        
        article =get_object_or_404(AutoTweet,seq=id)
        
        print("////////////////////")
        print(request.FILES)
        print("////////////////////")
        article.tweet=request.POST['content']
        article.reserve_date=request.POST['posting_time']
        article.tw_flg=0
        try:
            request.FILES['image_1']
            article.img_path1=request.FILES['image_1']
        except:
            pass
        
        try:
            request.FILES['image_2']
            article.img_path2=request.FILES['image_2']
        except:
            pass

        try:
            request.FILES['image_3']
            article.img_path3=request.FILES['image_3']
        except:
            pass

        try:
            request.FILES['image_4']
            article.img_path4=request.FILES['image_4']
        except:
            pass

        article.save()

    context = {
        'message': 'Update article ' + str(id),
        'article': article,
    }
    return render(request, 'front/detail.html', context)

def unfollow(request):#現在フォローしている人の中かフォロー解除
    return render(request, 'front/index.html')

