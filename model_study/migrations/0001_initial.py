# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u4f5c\u8005')),
                ('email', models.EmailField(default=None, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='\u5927\u6807\u9898')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='\u51fa\u7248\u65f6\u95f4')),
                ('authors', models.ManyToManyField(related_name='author_set', to='model_study.Author')),
            ],
            options={
                'managed': True,
                'ordering': ['pub_date', '-id'],
                'verbose_name_plural': '\u4e66\u7c4d\u67dc',
                'db_table': 'book',
                'verbose_name': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='\u4e66\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='\u56de\u590d')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_study.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_study.Number'),
        ),
    ]
