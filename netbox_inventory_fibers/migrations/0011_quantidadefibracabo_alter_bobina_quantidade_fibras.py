# Generated by Django 4.1.7 on 2023-03-05 18:56

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0084_staging'),
        ('netbox_inventory_fibers', '0010_rename_descricao_bobina_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantidadeFibraCabo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('quantidade', models.CharField(max_length=5)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Quantidade de Fibras no Cabo',
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='bobina',
            name='quantidade_fibras',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bobinas_to_quantidade', to='netbox_inventory_fibers.quantidadefibracabo'),
        ),
    ]
