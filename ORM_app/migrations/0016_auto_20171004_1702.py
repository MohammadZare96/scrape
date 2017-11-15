# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0015_auto_20171004_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bamilo',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bamiloids',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='digikala',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='digikalaids',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='digikalaurls',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
