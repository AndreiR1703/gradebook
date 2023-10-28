# Generated by Django 4.2.6 on 2023-10-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0003_grade_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='grade',
            name='added_by',
            field=models.CharField(default='prof1', max_length=100),
        ),
    ]
