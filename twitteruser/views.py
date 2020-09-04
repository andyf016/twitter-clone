from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import CustomUser
from twitteruser.forms import SignUpForm
from tweet.models import Tweet

@login_required
def index(request):
    current_user = CustomUser.objects.get(username=request.user)
    tweets = Tweet.objects.all()
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
            return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})


def follow_view(request, user_id):
    current_user = CustomUser.objects.get(username=request.user)
    to_follow = CustomUser.objects.filter(id=user_id).first()
    current_user.following.add(to_follow)
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unfollow_view(request, user_id):
    current_user = CustomUser.objects.get(username=request.user)
    to_unfollow = CustomUser.objects.filter(id=user_id).first()
    current_user.following.remove(to_unfollow)
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def profile_view(request, user_id):
    profile_user = CustomUser.objects.filter(id=user_id).first()
    followers = profile_user.following.all()
    # profile_tweets = Tweet.objects.filter(author=profile_user.username)
    tweet_count = Tweet.objects.filter(author_id=user_id).count()
    return render(request, 'profile.html', {"profile_user":profile_user, "tweet_count": tweet_count, "followers": followers})
    # add number of and possibly list of followers


"""
    @classmethod
    def follow(cls, current_user, following):
        following, created = cls.objects.get_or_create(
            current_user=current_user
        )
        following.owner.add(following)
"""