# Generated by Django 3.0.5 on 2020-05-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_trackuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='track_counts',
            field=models.IntegerField(default=0),
        ),
    ]
