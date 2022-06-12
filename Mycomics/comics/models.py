from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Comic(models.Model):
    title = models.CharField(max_length=128)
    image = models.URLField()
    comic = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comics = models.ForeignKey(Comic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    birthdate = models.DateTimeField(datetime)
    bio = models.TextField()
    image = models.URLField()


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Reader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score = models.IntegerField()

