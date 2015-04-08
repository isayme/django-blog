from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from blog.models import Post, Category, Tag, Comment

def index(req):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    posts = paginator.page(1)

    return render(req, 'blog/index.html', {'posts': posts})

def page(req, page_num=1):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(req, 'blog/page.html', {'posts': posts})

def category(req, category, page_num=1):
    try:
        config = Category.objects.get(name=category)
    except:
        config = None

    posts = Post.objects.filter(categories__name=category)
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(req, 'blog/category.html', {'posts': posts, 'config': config})

def tag(req, tag, page_num=1):
    try:
        config = Tag.objects.get(name=tag)
    except:
        config = None

    posts = Post.objects.filter(tags__name=tag)
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(req, 'blog/tag.html', {'posts': posts, 'config': config})

def post(req, year, month, path):
    try:
        post = Post.objects.get(slug=path)
    except:
        post = None
    return render(req, 'blog/post.html', {'post': post})