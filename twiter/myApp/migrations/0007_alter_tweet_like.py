# Generated by Django 4.1.4 on 2023-03-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_tweet_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='like',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
    ]
