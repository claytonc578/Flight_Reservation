# Generated by Django 3.1.2 on 2020-10-19 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20201018_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='plane_number',
            field=models.IntegerField(default=0),
        ),
    ]
