# Generated by Django 4.1.7 on 2023-03-09 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0012_alter_bobina_options_alter_fornecedor_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fibrarequisitada',
            old_name='id_requisicao',
            new_name='ordem_de_servico',
        ),
        migrations.RenameField(
            model_name='requisicao',
            old_name='bilhete_associado',
            new_name='ordem_de_servico',
        ),
    ]
