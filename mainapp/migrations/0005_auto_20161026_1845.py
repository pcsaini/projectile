# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20161025_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='u_bio',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_contact_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_current_college',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_current_degree',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_current_qualification',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_education_end_year',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_education_start_year',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_github',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_linkedin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_location',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_mentor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_prof_title',
        ),
        migrations.AlterField(
            model_name='student',
            name='u_dob',
            field=models.DateField(),
        ),
    ]
