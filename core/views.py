from django.shortcuts import render
from .models import Post, Tag
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.filter(slug=slug)
    return render(request, 'core/base.html', context={'post': post})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/profile_page.html', context={'user': user})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'core/tags.html', context={'tags': tags})
