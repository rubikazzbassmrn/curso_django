# Generated by Django 3.0 on 2020-02-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
    ]
