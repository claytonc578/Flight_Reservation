# Generated by Django 3.1.2 on 2020-10-22 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_passenger_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='passenger',
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.passenger')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.plane')),
            ],
        ),
    ]
