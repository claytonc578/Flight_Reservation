# Generated by Django 3.1.2 on 2020-10-22 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_remove_passenger_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='passenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.passenger'),
        ),
    ]
