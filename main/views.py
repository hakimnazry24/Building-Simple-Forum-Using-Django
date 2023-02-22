from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_view

def home(request):
    forums = Category.objects.all()
    
    context = {'forums':forums}
    return render(request, 'forums.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    update_view(request, post)

    context = {'post':post}
    return render(request, 'detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {'posts':posts}
    return render(request, 'posts.html', context)

