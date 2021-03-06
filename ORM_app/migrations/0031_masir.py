# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0030_auto_20171012_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(default='')),
                ('new_price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True)),
                ('old_price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True)),
                ('discount_percent', models.FloatField()),
                ('address', models.URLField(max_length=1000)),
                ('item_image', models.URLField(default='', max_length=1000)),
                ('masir_cat', models.TextField(default='')),
                ('brand', models.TextField(default='')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
