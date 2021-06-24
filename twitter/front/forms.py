from django import forms
from django.utils import timezone
# from .models import TweetArticle
from .models import AutoTweet
from PIL import Image
import bootstrap_datepicker_plus as datetimepicker
class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=140)

class ReservationTweetForm(forms.Form):
    # contents = forms.CharField(label='内容', max_length=140)
    # tweet_time = forms.DateTimeField(
    #     label='投稿時間',
    #     widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
    #     input_formats=['%Y-%m-%dT%H:%M']
    # )
    # images= forms.FileField()

    # contents.widget.attrs["class"] = "form-control"

    # model =  TweetArticle
    # fields = ['content', 'posting_time','image']
    model = AutoTweet
    content =  forms.CharField(label='内容', max_length=280,widget=forms.Textarea(attrs={ 'rows': '10'}))
    content.widget.attrs['class'] = 'form-control'

    posting_time = forms.DateTimeField(
        label='投稿時間',
        widget=datetimepicker.DateTimePickerInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    image= forms.ImageField(required=False,initial=None,widget=forms.FileInput(attrs={'multiple': True}))
    image_1= forms.ImageField(required=False)
    image_2= forms.ImageField(required=False)
    image_3= forms.ImageField(required=False)
    image_4= forms.ImageField(required=False)
    
    fields=('content','posting_time','image')
    


class AddFollow(forms.Form):
    Follow = forms.CharField(label='', max_length=140)