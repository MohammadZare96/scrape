# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0008_auto_20170925_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='digikala',
            name='classification',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='classification_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='classification_2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='item_image',
            field=models.URLField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='digikalaids',
            name='classification',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikalaids',
            name='classification_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikalaids',
            name='classification_2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikalaids',
            name='item_image',
            field=models.URLField(default='', max_length=1000),
        ),
    ]
