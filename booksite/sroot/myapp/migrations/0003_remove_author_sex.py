# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-12 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_author_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='sex',
        ),
    ]
