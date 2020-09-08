from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import CustomUser
from twitteruser.forms import SignUpForm
from tweet.models import Tweet
from notification.models import Notification

@login_required
def index(request):
    current_user = CustomUser.objects.get(username=request.user)
    tweets = Tweet.objects.filter(author__in=current_user.following.all()) | Tweet.objects.filter(author=current_user)
    tweets = tweets.order_by('-time_stamp')
    return render(request, 'index.html', {'tweets': tweets, 'current_user': current_user}) 


def signup_view(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username = data.get("username"),
                password = data.get("password"),
                bio = data.get("bio"),
                age = data.get("age"),
                location = data.get("location"),
                birthday = data.get("birthday"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("home"))
    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def follow_view(request, user_id):
    current_user = CustomUser.objects.get(username=request.user)
    to_follow = CustomUser.objects.filter(id=user_id).first()
    current_user.following.add(to_follow)
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow_view(request, user_id):
    current_user = CustomUser.objects.get(username=request.user)
    to_unfollow = CustomUser.objects.filter(id=user_id).first()
    current_user.following.remove(to_unfollow)
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def profile_view(request, user_id):
    profile_user = CustomUser.objects.filter(id=user_id).first()
    followers = profile_user.following.all()
    follower_count = profile_user.following.count()
    profile_tweets = Tweet.objects.filter(author_id=user_id)
    tweet_count = Tweet.objects.filter(author_id=user_id).count()
    return render(request, 'profile.html', {"follower_count": follower_count, "profile_user":profile_user, "tweet_count": tweet_count, "followers": followers, "profile_tweets": profile_tweets})
    


