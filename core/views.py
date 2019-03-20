from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.filter(slug=slug)
    return render(request, 'core/base.html', context={'post': post})
    