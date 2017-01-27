# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrillMe', '0003_auto_20170123_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='type',
            field=models.CharField(choices=[('FISH', 'FISH'), ('MEAT', 'MEAT'), ('VEG', 'VEGETABLE'), ('OTH', 'OTHER')], max_length=1),
        ),
    ]
