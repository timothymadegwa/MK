# Generated by Django 3.0.8 on 2020-10-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blogpost_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image_1',
            field=models.ImageField(upload_to='photos/blogs'),
        ),
    ]
