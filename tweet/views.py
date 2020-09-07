from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import CustomUser
from notification.models import Notification
import re


@login_required
def tweet_form_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newTweet = Tweet.objects.create(
                body=data.get('body'),
                author=request.user
            )
            matches = re.finditer(r'\@(\w+)', data.get("body"))
            
            for match in matches:
                users = CustomUser.objects.all()
                name = match.group(1)
                try:
                    user = CustomUser.objects.get(username=name)
                    Notification.objects.create(owner=user, mention_tweets=newTweet)
                except:
                    pass
            return HttpResponseRedirect(reverse('home'))
    form = TweetForm()
    return render(request, "new_tweet.html", {'form': form})

def tweet_view(request, tweet_id):
    current_tweet = Tweet.objects.get(id=tweet_id)
    return render(request, "tweet_detail.html", {'tweet':current_tweet})

def all_view(request):
    all_tweets = Tweet.objects.all().order_by('-time_stamp')
    return render(request, "all_tweets.html", {"all_tweets": all_tweets})

