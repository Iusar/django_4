# Generated by Django 3.1.2 on 2022-02-23 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20220223_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]
