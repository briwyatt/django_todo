# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-15 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20181115_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='comment',
            field=models.CharField(blank=True, max_length=280),
        ),
    ]
