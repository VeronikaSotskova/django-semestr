# Generated by Django 3.0.5 on 2020-04-23 18:50

from django.db import migrations, models
import django.db.models.deletion
import music.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Album title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/albums')),
                ('published', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'ordering': ['-published', 'author', 'title'],
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Genre name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/singers')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Singers',
                'ordering': ['name'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/songs')),
                ('track', models.FileField(upload_to='songs/%Y/%m/%d', validators=[music.validators.validate_file_extension])),
                ('published', models.DateField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', related_query_name='song', to='music.Album')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Genre')),
                ('singers', models.ManyToManyField(blank=True, null=True, related_name='songs', to='music.Singer')),
            ],
            options={
                'verbose_name_plural': 'Songs',
                'ordering': ['-published', 'title'],
                'get_latest_by': 'published',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', related_query_name='album', to='music.Singer'),
        ),
    ]