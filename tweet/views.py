from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import CustomUser


@login_required
def tweet_form_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data.get('body'),
                author=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = TweetForm()
    return render(request, "generic_form.html", {'form': form})

def tweet_view(request, tweet_id):
    current_tweet = Tweet.objects.get(id=tweet_id)
    return render(request, "tweet_detail.html", {'tweet':current_tweet})

