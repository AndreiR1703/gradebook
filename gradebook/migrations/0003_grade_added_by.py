# Generated by Django 4.2.6 on 2023-10-24 11:01

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0002_grade_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='added_by',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=100),
        ),
    ]
