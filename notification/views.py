from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

import re
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import CustomUser


def notification_view(request, user_id):
    notifications = Notification.objects.filter(owner=request.user)
    new_notifications = []
    for notification in notifications:
        if notification.read_flag == False:
            new_notifications.append(notification)
            notification.read_flag = True
            notification.save()
    return render(request, 'notifications.html', {'new_notifications': new_notifications})