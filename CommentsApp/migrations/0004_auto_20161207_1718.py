# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0003_auto_20161207_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parentId',
            new_name='parent',
        ),
    ]