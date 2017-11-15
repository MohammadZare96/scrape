# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0028_auto_20171011_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='BamiloUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='product_digikala',
            name='category2',
            field=models.TextField(default=''),
        ),
    ]