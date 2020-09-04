from django.db import models
from twitteruser.models import CustomUser
from tweet.models import Tweet

class Notification(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mention_tweets = models.ForeignKey(Tweet, null=True, default=None, on_delete=models.CASCADE, related_name='mentions')
    read_flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner)
