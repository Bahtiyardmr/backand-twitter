from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    image = models.FileField(upload_to='', default='wallpaper1', blank=True)
    bgimage = models.FileField(upload_to='', default='med2.jpg', blank=True)
    follow = models.ManyToManyField(User, related_name="takip")
    follower = models.ManyToManyField(User, related_name='takipci')

    def str(self):
        return self.user.username

class Tweet(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    text=models.TextField(("Text") , max_length=200)
    image=models.FileField(("image"), upload_to='', max_length=100, null=True)
    liked=models.ManyToManyField(User,default=None, blank=True,related_name='liked')
    
    
    @property
    def num_likes(self):
        return self.liked.all().count()

    
    
    
    
LIKE_CHOICES =(
       ('Like','Like'),
       ('Unlike','Unlike'),
   ) 

class Begeni(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    twiit=models.ForeignKey(Tweet, verbose_name=("Tweet"), on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)
    
    
