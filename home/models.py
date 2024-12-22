
from django.db import models
from django.contrib.auth.models import User

# User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    isVerified= models.BooleanField(blank=True, default=False)
    # Until i pip pillow -> profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.user.username


