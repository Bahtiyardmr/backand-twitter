# Generated by Django 4.1.4 on 2023-03-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_tweet_folowed_folow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='folowed',
        ),
        migrations.DeleteModel(
            name='Folow',
        ),
    ]
