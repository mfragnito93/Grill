# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('F', 'FISH'), ('M', 'MEAT'), ('V', 'VEGETABLE'), ('O', 'OTHER')], max_length=1)),
                ('timer', models.DurationField()),
            ],
        ),
    ]
