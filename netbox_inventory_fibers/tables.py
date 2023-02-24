import django_tables2 as tables

from netbox.tables import NetBoxTable, columns #, ChoiceFieldColumn
from .models import *


class FornecedorTable(NetBoxTable):
    nome_fornecedor = tables.Column(
        linkify=True
    )
    # bobinas_count = columns.LinkedCountColumn(
    #     viewname='wireless:wirelesslan_list',
    #     url_params={'group_id': 'pk'},
    #     verbose_name='Bobinas'
    # )
    class Meta(NetBoxTable.Meta):
        model = Fornecedor
        # 225343 o 'fields' torna as opções disponíveis em 'configure table'
        fields = ('pk', 'id', 'nome_fornecedor', 'email', 'telefone', 'endereco_site', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'nome_fornecedor', 'telefone', 'endereco_site')


class TipoBobinaTable(NetBoxTable):
    descricao = tables.Column(
        linkify=True
    )
    # bobinas_count = columns.LinkedCountColumn(
    #     viewname='wireless:wirelesslan_list',
    #     url_params={'group_id': 'pk'},
    #     verbose_name='Bobinas'
    # )
    class Meta(NetBoxTable.Meta):
        model = TipoBobina
        fields = ('pk', 'id', 'descricao', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'descricao')