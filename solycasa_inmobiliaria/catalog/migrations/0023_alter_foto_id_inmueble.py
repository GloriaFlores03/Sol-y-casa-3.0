# Generated by Django 4.1.2 on 2023-02-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_remove_inmueble_ubicacion_maps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='id_inmueble',
            field=models.IntegerField(null=True),
        ),
    ]