# Generated by Django 4.1.2 on 2023-02-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_empleado_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id_empleados'], 'permissions': (('Permisos_Empleados', 'edit inmueble'),)},
        ),
    ]