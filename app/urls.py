from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('blogs', views.blogs, name='blogs'),
    path('videos', views.videos, name='videos'),
    path('contact', views.contact, name='contact'),    
]