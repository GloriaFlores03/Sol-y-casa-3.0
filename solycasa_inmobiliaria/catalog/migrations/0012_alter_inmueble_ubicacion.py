# Generated by Django 4.1.2 on 2023-02-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_inmueble_hipoteca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='ubicacion',
            field=models.CharField(max_length=200),
        ),
    ]
