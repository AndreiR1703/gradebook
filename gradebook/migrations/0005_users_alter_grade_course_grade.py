# Generated by Django 4.2.6 on 2023-10-28 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0004_grade_student_name_alter_grade_added_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('is_teacher', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='grade',
            name='course_grade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10, message='Grade must be less than or equal to 10.')]),
        ),
    ]
