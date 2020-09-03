from tweet.models import Tweet
from django import forms


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['body']