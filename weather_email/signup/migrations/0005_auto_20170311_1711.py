# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-11 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20161226_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='location',
            field=models.CharField(max_length=250),
        ),
    ]
