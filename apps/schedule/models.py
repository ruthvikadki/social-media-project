from django.db import models
from django.utils import timezone

from apps.user.models import User


class Platform(models.TextChoices):
    INSTAGRAM = ('IG', 'Instagram')
    FACEBOOK = ('FB', 'Facebook')
    TWITTER = ('X', 'Twitter')


class PlatformAuth(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    platform = models.CharField(max_length = 15, choices=Platform.choices, default = Platform.INSTAGRAM)
    credentials = models.JSONField()

    def __str__(self):
        return self.username


class SchedulePost(models.Model):
    post_title = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20,choices=Platform.choices, default = Platform.INSTAGRAM)
    post_content = models.TextField(max_length = 20)
    schedule_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
