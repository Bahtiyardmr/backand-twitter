# Generated by Django 4.1.4 on 2023-03-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_tweet_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='like',
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(null=True, verbose_name='likes'),
        ),
    ]
