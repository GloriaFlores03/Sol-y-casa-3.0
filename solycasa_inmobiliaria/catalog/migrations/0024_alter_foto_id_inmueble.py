# Generated by Django 4.1.2 on 2023-02-22 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_alter_foto_id_inmueble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='id_inmueble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.inmueble'),
        ),
    ]
