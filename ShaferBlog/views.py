from django.shortcuts import render
from .models import Post #we can just use '.' since we are directory-fellows
#from django.http import HttpResponse
#no longer needed cuz we use render

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'ShaferBlog/home.html', context)


def about(request):
    return render(request, 'ShaferBlog/about.html', {'title': 'About'})
