# Generated by Django 4.2.1 on 2023-06-17 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_tipoenvio_alter_venta_fecha_envio_venta_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 16, 33, 39, 448540)),
        ),
    ]
