# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-09 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('name',), 'verbose_name': 'fab_dish', 'verbose_name_plural': 'fab_dishes'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ('name',), 'verbose_name': 'fab_restaurant', 'verbose_name_plural': 'fab_restaurants'},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]