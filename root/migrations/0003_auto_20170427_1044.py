# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20170423_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': '房间'},
        ),
    ]