# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0027_auto_20171007_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_digikala',
            name='brand',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product_digikala',
            name='brand_fa',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product_digikala',
            name='masir_cat',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='bamiloids',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='pid',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='digikala_details',
            name='product_id',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_bamilo',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_bamilo',
            name='new_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_bamilo',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_digikala',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_digikala',
            name='new_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_digikala',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product_digikala',
            name='product_id',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='torob',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='torob',
            name='new_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='torob',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=1000, null=True),
        ),
    ]
