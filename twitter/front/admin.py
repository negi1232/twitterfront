from django.contrib import admin
from front.models import AutoTweet
from .models import FollowList
#from .models import TargetList
from .models import TargetInfo
admin.site.register(AutoTweet)
admin.site.register(FollowList)
admin.site.register(TargetInfo)