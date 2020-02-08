from django.shortcuts import render
#from django.http import HttpResponse
#no longer needed cuz we use render

posts = [
    {
        'author': 'ClarkS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'ClarkS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 31, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'ShaferBlog/home.html', context)


def about(request):
    return render(request, 'ShaferBlog/about.html', {'title': 'About'})
