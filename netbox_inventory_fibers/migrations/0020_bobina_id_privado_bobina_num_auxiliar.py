# Generated by Django 4.1.7 on 2023-03-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0019_rename_total_metragem_bobina_metragem_cadastrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobina',
            name='id_privado',
            field=models.CharField(default='empty', max_length=50),
        ),
        migrations.AddField(
            model_name='bobina',
            name='num_auxiliar',
            field=models.PositiveIntegerField(default=0),
        ),
    ]