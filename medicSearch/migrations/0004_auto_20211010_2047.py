# Generated by Django 3.2.8 on 2021-10-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0003_rename_adress_address_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='specialties',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
