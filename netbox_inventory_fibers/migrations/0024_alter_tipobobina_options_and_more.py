# Generated by Django 4.1.7 on 2023-03-14 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0023_alter_fibrarequisitada_imagem_corte_cabo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipobobina',
            options={'ordering': ('id',), 'verbose_name': 'Status'},
        ),
        migrations.AlterField(
            model_name='fibrarequisitada',
            name='imagem_corte_cabo',
            field=models.ImageField(unique=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endereco_site',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome_fornecedor',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='quantidadefibracabo',
            name='quantidade',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='requisicao',
            name='ordem_de_servico',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='tipobobina',
            name='descricao',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
