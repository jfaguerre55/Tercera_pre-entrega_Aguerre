# Generated by Django 4.1.6 on 2023-02-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='area',
            field=models.CharField(max_length=20),
        ),
    ]
