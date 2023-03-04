from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    text=models.TextField(("Text") , max_length=200)
    image=models.FileField(("image"), upload_to='', max_length=100, null=True)