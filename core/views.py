from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.contrib.auth.models import User
from .forms import CommentForm, PostForm


# Create your views here.

def index(request):
    posts = Post.objects.all()

    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
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


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail', slug=post.slug)
        
       
        else:
            form = CommentForm()
        template = 'add_comment.html'
        context = {'forms': form}
        return render(request, template, context)
        