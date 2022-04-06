from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(blank=True, max_length=255)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')
    bio_data = models.TextField(blank=True)
    social_site = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)
