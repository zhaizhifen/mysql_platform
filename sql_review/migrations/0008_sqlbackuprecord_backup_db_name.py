# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_review', '0007_auto_20170731_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlbackuprecord',
            name='backup_db_name',
            field=models.CharField(default='', max_length=40, verbose_name='\u5907\u4efd\u6570\u636e\u5e93\u540d'),
        ),
    ]
