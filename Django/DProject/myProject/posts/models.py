# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Custom Manager to get only published posts
class PublishedManager(models.Manager):


    def get_queryset(self):
        return super(PublishedManager, self)\
            .get_queryset().filter(status='published')

    
  
def upload_location(instance, filename):
    return 'imgs/{0}/{1}'.format(instance.title, filename)


class post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_active= models.BooleanField(default = True)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            )
     # The default manager
    objects = models.Manager()
    # Custom made manager
    published = PublishedManager()

    # image = models.ImageField(upload_to=upload_location,
    #         null=True,
    #         blank=True,
    #         )
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.slug


    def get_absolute_url(self):
        return reverse('posts:post_detail_view',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])