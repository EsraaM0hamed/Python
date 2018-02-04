# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import post

def post_lists_view (request):
    posts=post.objects.all()
    context={'posts':posts}
    return render(request,'list.html',context)
