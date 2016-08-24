# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0022_auto_20160729_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affiliationversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='associationversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='personemailversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughawardentitiesversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughawardsversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughidentifiersversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughlinksversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughtagsversion',
            options={},
        ),
        migrations.AlterModelOptions(
            name='throughvenuesversion',
            options={},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='url',
        ),
        migrations.RemoveField(
            model_name='tagversion',
            name='url',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='name',
            field=models.TextField(),
        ),
    ]
