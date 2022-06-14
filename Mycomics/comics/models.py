from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Comic(models.Model):
    """ This class for comic attributes """
    title = models.CharField(max_length=128)
    image = models.URLField()
    comic = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])


class Feedback(models.Model):
    """ This class for feedback attributes """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    """ This class for profile attributes """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    birthdate = models.DateTimeField(datetime)
    bio = models.TextField()
    image = models.URLField()
    score = models.IntegerField()


class Favorite(models.Model):
    """ This class for favorite attributes """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)


