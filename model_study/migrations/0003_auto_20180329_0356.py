# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_study', '0002_auto_20180329_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='number',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_study.ClassNumber'),
        ),
    ]