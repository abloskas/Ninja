# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nip', '0004_auto_20180329_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='slack',
            field=models.TextField(null=True),
        ),
    ]
