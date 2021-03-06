# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrillMe', '0006_remove_fooditem_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='hours',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fooditem',
            name='minutes',
            field=models.IntegerField(default=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fooditem',
            name='seconds',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
