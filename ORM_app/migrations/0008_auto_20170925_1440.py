# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0007_bamilo_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='bamilo',
            name='classification_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='bamilo',
            name='classification_2',
            field=models.TextField(default=''),
        ),
    ]