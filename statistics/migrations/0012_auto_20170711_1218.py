# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('statistics', '0011_auto_20170710_1536'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mysqlinstance',
            unique_together=set([('ip', 'port')]),
        ),
    ]
