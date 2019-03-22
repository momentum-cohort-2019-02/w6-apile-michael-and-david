from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Tag
from .forms import PostForm


# Create your views here.

def index(request):
    posts = Post.objects.all()

    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                request,
                f"Thank you for your input!"
            )
            return redirect(to='index')

    form = PostForm()

    return render(request, 'core/index.html', context={'posts': posts, 'form':form})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'core/post_detail.html', context={'post': post})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/profile_page.html', context={'user': user})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'core/tags.html', context={'tags': tags})

def tagged_list(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    return render(request, 'core/tagged_list.html', context={'posts': posts})
