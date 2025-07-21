from django.shortcuts import render
from django.http import HttpResponse

#dummy data
posts = [{
    "author": "Ali Rezaei",
    "title": "Introduction to Python",
    "content": "Python is a simple and powerful programming language.",
    "date_posted": "2025-07-21"
        },
         {
    "author": "Corey Ms",
    "title": "Blog Post",
    "content": "first post content.",
    "date_posted": "2024-07-21"
         },



]
# Create your views here.
def home(request):
    #return HttpResponse('<h1>welcome to my page</h1>')
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)
def about(request):
    return render(request, 'blog/about.html')




