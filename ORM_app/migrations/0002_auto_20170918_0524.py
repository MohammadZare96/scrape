# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BamiloIds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TorobIds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='digikalaids',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]