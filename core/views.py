from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Comment
from django.contrib.auth.models import User
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


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
    paginator = Paginator(posts, 20)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    return render(request, 'core/index.html', context={'posts': posts, 'form':form})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()
    return render(request, 'core/post_detail.html', context={'post': post, 'comments':comments})

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.authored_posts.all()

    paginator = Paginator(posts, 20)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    return render(request, 'core/profile_page.html', context={'user': user, 'posts': posts})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'core/tags.html', context={'tags': tags})

def tagged_list(request, slug):
    posts = Post.objects.filter(tags__slug=slug)

    paginator = Paginator(posts, 20)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    return render(request, 'core/tagged_list.html', context={'posts': posts, 'tag': slug})


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenting_on = post 
            comment.save()
            return redirect('post_detail', slug=post.slug)
        
       
   
    form = CommentForm()
    template = 'core/add_comment.html'
    context = {'form': form, 'post': post }

    return render(request, template, context)
    
@login_required
def like_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.user not in post.liked_by.all():
        post.liked_by.add(request.user)
    else:
        post.liked_by.remove(request.user)
    next_page = request.POST.get('next', '/')
    return redirect(next_page)

@login_required
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    next_page = request.POST.get('next', '/')
    return redirect(next_page)
   