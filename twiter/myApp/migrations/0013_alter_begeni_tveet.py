# Generated by Django 4.1.4 on 2023-03-08 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_remove_tweet_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='begeni',
            name='tveet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.tweet', verbose_name='Tweet'),
        ),
    ]
