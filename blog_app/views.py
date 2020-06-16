# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .forms import PostAddForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.all().order_by('-created_at')
        posts = posts.filter(
        Q(title__icontains=query)|
        Q(user__username__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all().order_by('-created_at')  
    return render(request, 'blog_app/index.html', {'posts': posts, 'query': query,})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/detail.html', {'post': post})

@login_required
def add(request):
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog_app:index')
    else:
       form = PostAddForm()
    return render(request, 'blog_app/add.html', {'form': form})

@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_app:detail', post_id=post.id)
    else:
        form = PostAddForm(instance=post)
    return render(request, 'blog_app/edit.html', {'form': form, 'post':post })

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('blog_app:index')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]
            if myself:
                recipients.append(email)
            try:
                send_mail(name, message, email, recipients)
            except BadHeaderError:
                 return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('blog_app:done')
    else:
        form = ContactForm()
    return render(request, 'blog_app/contact.html', {'form': form})

def done(request):
    return render(request, 'blog_app/done.html')