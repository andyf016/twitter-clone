from django.db import models
from twitteruser.models import CustomUser
from django.utils import timezone

class Tweet(models.Model):
    body = models.TextField(max_length=140)
    time_stamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

