# Generated by Django 4.1.2 on 2023-02-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_inmueble_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='hipoteca',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
