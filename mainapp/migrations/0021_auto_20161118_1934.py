# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 19:34
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20161118_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Django', 'Django'), ('Java', 'Java')], max_length=6000),
        ),
    ]