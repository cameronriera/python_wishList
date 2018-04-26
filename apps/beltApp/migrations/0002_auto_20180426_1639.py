# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_products', to='beltApp.User')),
                ('favorited_by', models.ManyToManyField(related_name='favorites', to='beltApp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='quotable',
            name='favorited_by',
        ),
        migrations.RemoveField(
            model_name='quotable',
            name='posted_by',
        ),
        migrations.DeleteModel(
            name='Quotable',
        ),
    ]