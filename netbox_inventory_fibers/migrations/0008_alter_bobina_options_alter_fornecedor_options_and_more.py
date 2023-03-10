# Generated by Django 4.1.7 on 2023-02-28 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0007_alter_bobina_tipo_bobina'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bobina',
            options={'ordering': ('id',), 'verbose_name': 'Bobina'},
        ),
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'ordering': ('nome_fornecedor',), 'verbose_name': 'Fornecedor'},
        ),
        migrations.AlterModelOptions(
            name='requisicao',
            options={'ordering': ('id',), 'verbose_name': 'Requisições'},
        ),
        migrations.AlterModelOptions(
            name='tipobobina',
            options={'ordering': ('id',), 'verbose_name': 'Tipos de Bobina'},
        ),
        migrations.AlterField(
            model_name='bobina',
            name='nome_fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bobinas_to_fornecedor', to='netbox_inventory_fibers.fornecedor'),
        ),
    ]
