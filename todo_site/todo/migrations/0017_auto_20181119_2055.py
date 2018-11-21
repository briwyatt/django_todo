# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_restaurant_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('visited', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=280)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]