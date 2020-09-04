from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import CustomUser, FollowingUser
from twitteruser.forms import SignUpForm
from tweet.models import Tweet


def index(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html', {'tweets': tweets}) 


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
    following = FollowingUser.objects.get_or_create(owner=request.user, is_following=is_following.set(user_id))
    

"""
    @classmethod
    def follow(cls, current_user, following):
        following, created = cls.objects.get_or_create(
            current_user=current_user
        )
        following.owner.add(following)
"""