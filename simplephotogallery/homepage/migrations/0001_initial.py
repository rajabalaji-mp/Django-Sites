# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-07 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_caption', models.CharField(max_length=150)),
                ('photo_description', models.CharField(max_length=1000)),
                ('photo_file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
