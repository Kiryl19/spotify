# Generated by Django 3.1.4 on 2020-12-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20201208_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favourite_artists',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favourite_genres',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='songs_liked',
        ),
    ]