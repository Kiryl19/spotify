# Generated by Django 3.1.4 on 2020-12-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20201208_2115'),
        ('authorization', '0005_auto_20201208_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourite_artists',
            field=models.ManyToManyField(blank=True, to='music.Artist'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favourite_genres',
            field=models.ManyToManyField(blank=True, to='music.Genre'),
        ),
        migrations.AddField(
            model_name='profile',
            name='songs_liked',
            field=models.ManyToManyField(blank=True, to='music.Song'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
