# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0007_auto_20161207_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(),
        ),
    ]