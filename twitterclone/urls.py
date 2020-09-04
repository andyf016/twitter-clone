"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as userviews
from authentication import views as authviews
from tweet import views as tweetviews

urlpatterns = [
    path('', userviews.index, name='home'),
    path('profile/<int:user_id>', userviews.profile_view, name='profile'),
    path('following/<int:user_id>/', userviews.follow_view, name='follow'),
    path('unfollow/<int:user_id>/', userviews.unfollow_view),
    path('newtweet/', tweetviews.tweet_form_view, name='newtweet'),
    path('tweet/<int:tweet_id>', tweetviews.tweet_view, name='tweet'),
    path('login/', authviews.login_view, name='login'),
    path('logout/', authviews.logout_view, name='logout'),
    path('signup/', userviews.signup_view, name='signup'),
    path('admin/', admin.site.urls),
]
