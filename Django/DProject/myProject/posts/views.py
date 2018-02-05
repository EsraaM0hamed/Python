# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, NameForm
from django.urls import reverse
from .models import post


# def post_list_view(request):
#     # get only published Posts
#     posts = Post.published.all()
#     context = {'posts': posts}
#     return render(request, 'posts/list.html', context)


def post_detail_view(request, year, month, day, slug):
    post = get_object_or_404(post, slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'detail.html', {'post': post})


def post_list_view(request):
    list_objects = post.published.all()
    paginator = Paginator(list_objects, 1)
    page = request.GET.get('mypage')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'posts': posts})

# update, del and image with post

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        # message success
        messages.success(request, "Successfully Created")
        return redirect(reverse('posts:post_list_view'))
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request, post_id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, "<a href='#'>Item</a> Updated", extra_tags='html_safe')
        return redirect(reverse('posts:post_update', args=[instance.id]))

    context = {
       
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, post_id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=post_id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:post_list_view")



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'myform': form})


