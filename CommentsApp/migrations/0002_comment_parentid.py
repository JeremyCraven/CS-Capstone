# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='CommentsApp.Comment'),
        ),
    ]
