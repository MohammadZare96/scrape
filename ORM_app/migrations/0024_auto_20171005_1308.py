# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0023_auto_20171005_1148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Digikala',
            new_name='Digikala_details',
        ),
        migrations.RenameModel(
            old_name='Bamilo',
            new_name='Product_Bamilo',
        ),
        migrations.RenameModel(
            old_name='DigikalaIds',
            new_name='Product_Digikala',
        ),
    ]
