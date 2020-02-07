from django.shortcuts import render
#from django.http import HttpResponse
#no longer needed cuz we use render


def home(request):
    return render(request, 'ShaferBlog/home.html')


def about(request):
    return render(request, 'ShaferBlog/about.html')
