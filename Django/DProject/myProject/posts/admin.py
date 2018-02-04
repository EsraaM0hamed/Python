# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import post;


class postAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status','publish')
    list_filter=('status','created','publish','author')
    search_fields=('title',)
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['-publish']
    
admin.site.register(post,postAdmin);            # ,to know that it is tupple
