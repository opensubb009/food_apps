# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180712_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuisinetype',
            options={'ordering': ('name',), 'verbose_name_plural': 'Cuisine Types'},
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]