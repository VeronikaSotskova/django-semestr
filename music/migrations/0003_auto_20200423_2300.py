# Generated by Django 3.0.5 on 2020-04-23 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200423_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', related_query_name='songs', to='music.Genre'),
        ),
    ]
