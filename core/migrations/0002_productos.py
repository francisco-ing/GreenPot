# Generated by Django 4.2.1 on 2023-06-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]
