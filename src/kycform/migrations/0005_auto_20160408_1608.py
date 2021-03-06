# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kycform', '0004_auto_20160408_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='nominee_relation',
            field=models.CharField(choices=[('son', 'Son'), ('daughter', 'Daughter'), ('husband', 'Husband'), ('father', 'Father'), ('mother', 'Mother'), ('brother', 'Brother')], default='son', max_length=7),
        ),
    ]
