# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 17:40
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('beltApp', '0002_auto_20180426_1639'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('productManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
