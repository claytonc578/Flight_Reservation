# Generated by Django 3.1.2 on 2020-10-22 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20201021_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='user',
        ),
    ]
