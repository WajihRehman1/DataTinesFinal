from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.validators import UnicodeUsernameValidator


class UserProfileInfo(models.Model):
    fname=models.CharField(max_length=256)
    lname=models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    contact = models.BigIntegerField(max_length=11)
    email = models.EmailField()
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    team = models.CharField(max_length=20)
    projects=models.CharField(max_length=200)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
