# Generated by Django 4.1.4 on 2023-03-08 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0017_tweet_tweet_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Begeni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twiit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.tweet', verbose_name='Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
