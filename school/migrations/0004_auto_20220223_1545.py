# Generated by Django 3.1.2 on 2022-02-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220223_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher'),
        ),
    ]
