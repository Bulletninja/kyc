# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20160329_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branchinfo',
            name='date_info',
        ),
    ]
