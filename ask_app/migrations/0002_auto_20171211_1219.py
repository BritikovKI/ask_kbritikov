# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='head',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagtext',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
