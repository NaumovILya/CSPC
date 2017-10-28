# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CSPCApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractendinfo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
