from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import CustomUser, FollowingUser
from twitteruser.forms import SignUpForm

# Create your views here.
"""
    @classmethod
    def follow(cls, current_user, following):
        following, created = cls.objects.get_or_create(
            current_user=current_user
        )
        following.owner.add(following)
"""