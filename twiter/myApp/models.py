from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    text=models.TextField(("Text") , max_length=200)
    image=models.FileField(("image"), upload_to='', max_length=100, null=True)
    tweet_likes=models.IntegerField(("tweet_Likes"),default=0)
    
    

class Begeni(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    twiit=models.ForeignKey(Tweet, verbose_name=("Tweet"), on_delete=models.CASCADE)