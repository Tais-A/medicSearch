# Generated by Django 3.2.8 on 2021-10-10 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0002_auto_20211010_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='adress',
            new_name='address',
        ),
    ]
