# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-17 05:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
