# Generated by Django 4.1.7 on 2023-03-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0022_remove_bobina_id_privado_remove_bobina_num_auxiliar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibrarequisitada',
            name='imagem_corte_cabo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
