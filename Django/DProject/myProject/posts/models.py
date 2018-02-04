from __future__ import unicode_literals

from django.db import models;
from django.utils import timezone;
from django.contrib.auth.models import User



class post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))


    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts')
    body=models.TextField();
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class meta:
        ordering=('-publish',)# - mean akr taree5 publish 
    def __str__(self):
        return self.slug 
    
