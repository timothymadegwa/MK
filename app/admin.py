from django.contrib import admin
from .models import Contact, Video, BlogPost

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','f_name', 'email')
    list_display_links = ('id','f_name', 'email')

admin.site.register(Contact, ContactAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','link')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)

admin.site.register(Video, VideoAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','author',)
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title',)

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.site_header = "MK Consultancy Admin"
