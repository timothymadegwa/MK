from django.db import models
from datetime import datetime, date

# Create your models here.

class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default='number')
    message = models.TextField()
    posted = models.DateField(default=datetime.now)

    def __str__(self):
        return self.f_name + self.l_name

class BlogPost(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    paragraph_1 = models.TextField(blank=False, null=False)
    image_1 = models.ImageField(upload_to='photos/blogs', null=False, blank=False)
    caption_1 = models.CharField(max_length=100, blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    image_2 = models.ImageField(upload_to='photos/blogs', null=True, blank=True)
    caption_2 = models.CharField(max_length=100, blank=True, null=True)
    paragraph_3 = models.TextField(blank=True, null=True)
    image_3 = models.ImageField(upload_to='photos/blogs', null=True, blank=True)
    caption_3 = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=date.today)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Video(models.Model):

    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title