# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0002_auto_20171211_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
