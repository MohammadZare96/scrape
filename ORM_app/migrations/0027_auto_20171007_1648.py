# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0026_category_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='digikala_details',
            name='masir_cat',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product_bamilo',
            name='masir_cat',
            field=models.TextField(default=''),
        ),
    ]
