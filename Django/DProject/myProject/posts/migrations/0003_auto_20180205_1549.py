# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180205_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
