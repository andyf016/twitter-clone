from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=240, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=180, null=True, blank=True)
    foll

    def __str__(self):
        return self.username

class FollowingUser(models.Model):
    # modeled after code from unicdev on stackoverflow.com
    user_id = models.ForeignKey("CustomUser", related_name="following")
    following_user_id = models.ForeignKey("CustomUser", related_name="followers")
    created = models.DateField(default=timezone.now)

    class Meta:
        # Prohibit following the same user more than once
        models.UniqueConstraint(
            fields=["user_id", "following_user_id"], 
            name='unique_following'
            )

    def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"