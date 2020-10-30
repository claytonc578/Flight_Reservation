# Generated by Django 3.1.2 on 2020-10-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_auto_20201026_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='col',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='row',
        ),
        migrations.AddField(
            model_name='ticket',
            name='column',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='ticket',
            name='row',
            field=models.IntegerField(default=0),
        ),
    ]