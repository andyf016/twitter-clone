from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=240, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=180, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    # Ask about logic in model

    def __str__(self):
        return self.username

class FollowingUser(models.Model):
    # modeled after code from unicdev on stackoverflow.com
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=False, related_name="owner")
    is_following = models.ManyToManyField(CustomUser, editable=False, related_name="followers")
    created = models.DateField(default=timezone.now, editable=False)



    def __str__(self):
        f"{self.user_id}'s following list"