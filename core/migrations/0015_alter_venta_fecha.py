# Generated by Django 4.2.1 on 2023-07-04 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 19, 49, 35, 934841)),
        ),
    ]