from django.shortcuts import render, get_object_or_404
from .models import Contact, BlogPost, Video
from django.contrib import messages
#from smtplib import SMTP, SMTP_SSL

# Create your views here.

def index(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-views')[:3]
    videos = Video.objects.filter(is_published=True)[:3]
    context = {
        'blogs' : blogs,
        'videos' : videos,
    }
    return render(request, 'app/index.html', context)

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def blogs(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-id')
    context = {
        'blogs' : blogs,
    }
    return render(request, 'app/blogs.html', context)

def blog(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    blogs = BlogPost.objects
    recent_blogs = blogs.filter(is_published=True).order_by('-id').exclude(slug=slug)[:3]
    popular_blogs = blogs.filter(is_published=True).order_by('-views').exclude(slug=slug)[:3]
    views = blog.views
    blog.views = views + 1
    blog.save()

    context = {
        'blog' : blog,
        'recent_blogs' : recent_blogs,
        'popular_blogs' : popular_blogs
    }
    return render(request, 'app/blog.html', context)

def videos(request):
    videos = Video.objects.filter(is_published=True)
    context = {
        'videos' : videos
    }
    return render(request, 'app/videos.html', context)
    
def contact(request):
    if request.method == 'POST':
        f_name = request.POST['firstName']
        l_name = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(f_name=f_name, l_name=l_name, email=email, phone=phone, message=message)
        contact.save()
        message = 'Thank you for contacting us '+f_name+', We will get back to you shortly'
        messages.success(request, message)
        '''
        send_to = ['admin@mkc.co.ke']
        send_to.append(email)
        server = SMTP_SSL('mail.timdev.co.ke' , 465)
        #server.starttls()
        server.login('contact@timdev.co.ke', 'Kibukamusoke1')
        server.sendmail('contact@timdev.co.ke', send_to, message)
        server.quit()'''
        return render(request, 'app/contact.html')
    return render(request, 'app/contact.html')
