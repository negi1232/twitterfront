from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('priorityfollow', views.priorityfollow, name='priorityfollow'),
    path('followlistdel/<int:id>',views.followlistdel, name='followlistdel'),
    path('follow_list', views.follow_list, name='follow_list'),
    path('toppage', views.toppage, name='toppage'),
    path('autotweet', views.autotweet, name='autotweet'),
    path('posttweetview', views.posttweetview, name='posttweetview'),
    path('unfollow', views.unfollow, name='unfollow'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('accountdetail/<int:id>', views.accountdetail, name='accountdetail'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    
    
    path('tweetview', views.tweetview, name='tweetview'),
    
    
]