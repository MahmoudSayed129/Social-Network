from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Posts(models.Model):
    post = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="user")
    username = models.CharField(max_length=256, default="")
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} posted"
    

class Comments (models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateTimeField(default=timezone.now)
    # post = models.ManyToManyField(Posts, blank=True)
    post_id = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user.username} commented on post of id {self.id}"

class Likes(models.Model):
    #post = models.ManyToManyField(Posts, blank=True)
    post_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} liked post of id {self.post_id}"

class Follwers(models.Model):
    follower = models.CharField(max_length=256)
    follwing = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.follower} is following {self.follwing}"
