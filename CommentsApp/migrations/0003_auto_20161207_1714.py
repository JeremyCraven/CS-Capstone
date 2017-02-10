# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0002_comment_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comment', to='CommentsApp.Comment'),
        ),
    ]
