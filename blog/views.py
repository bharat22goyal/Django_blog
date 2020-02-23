from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=[
    {
        'author':'Bharat Goyal',
        'title':'Blog Post1',
        'content':'First post content',
        'date':'22 Feb 2020'
    },
    {
        'author':'Chetan',
        'title':'Blog Post2',
        'content':'Second post content',
        'date':'22 Feb 2020'
    }
]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
