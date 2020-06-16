# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/index.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/detail.html', {'post': post})