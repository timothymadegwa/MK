# Generated by Django 3.0.8 on 2020-10-28 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('paragraph_1', models.TextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='photos/blogs')),
                ('caption_1', models.CharField(blank=True, max_length=100, null=True)),
                ('paragraph_2', models.TextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='photos/blogs')),
                ('caption_2', models.CharField(blank=True, max_length=100, null=True)),
                ('paragraph_3', models.TextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='photos/blogs')),
                ('caption_3', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
                ('link', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]