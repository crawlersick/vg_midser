# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vgitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('ipadd', models.CharField(max_length=20)),
                ('ovpnfile', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
