# Generated by Django 4.1.2 on 2023-02-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_inmueble_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='subir_foto_a',
            field=models.ImageField(null=True, upload_to='fotos_inmuebles/fotos_alquilar'),
        ),
        migrations.AddField(
            model_name='foto',
            name='subir_foto_c',
            field=models.ImageField(null=True, upload_to='fotos_inmuebles/fotos_compra'),
        ),
    ]
