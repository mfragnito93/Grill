# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 00:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GrillMe', '0005_auto_20170123_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='timer',
        ),
    ]
