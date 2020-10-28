from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def blogs(request):
    return render(request, 'app/blogs.html')

def videos(request):
    return render(request, 'app/videos.html')
    
def contact(request):
    return render(request, 'app/contact.html')
