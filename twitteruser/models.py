from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=240, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=180, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    # Ask about logic in model
    def get_following(self):
        following = FollowingUser.objects.filter(user_id=self.user_id)
        return following
    
    def get_followers(self):
        followers = FollowingUser.objects.filter(following_user_id=self.following_user_id)
        return  followers

    def __str__(self):
        return self.username

class FollowingUser(models.Model):
    # modeled after code from unicdev on stackoverflow.com
    user_id = models.ForeignKey("CustomUser", editable=False, related_name="following")
    following_user_id = models.ForeignKey("CustomUser", editable=False, related_name="followers")
    created = models.DateField(default=timezone.now, editable=False)

    class Meta:
        # Prohibit following the same user more than once
        models.UniqueConstraint(
            fields=["user_id", "following_user_id"], 
            name='unique_following'
            )

    def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"