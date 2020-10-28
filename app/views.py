from django.shortcuts import render
from .models import Contact, BlogPost,Video
from django.contrib import messages
#from smtplib import SMTP, SMTP_SSL

# Create your views here.

def index(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-id')
    videos = Video.objects.filter(is_published=True)
    context = {
        'blogs' : blogs,
        'videos' : videos,
    }
    return render(request, 'app/index.html')

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
