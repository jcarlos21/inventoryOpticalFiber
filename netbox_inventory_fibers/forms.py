from netbox.forms import NetBoxModelForm
from .models import Fornecedor, TipoBobina, Bobina, Requisicao
from utilities.forms.fields import CommentField, ModelMultipleChoiceField, DynamicModelChoiceField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm


class FornecedorForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = Fornecedor
        fields = ('nome_fornecedor', 'email', 'telefone', 'endereco_site', 'comments')


class TipoBobinaForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = TipoBobina
        fields = ('descricao', 'comments')


class BobinaForm(TipoBobinaForm, NetBoxModelForm):
    fieldsets = (
        ('Parâmetros da Bobina', ('modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'tipo_bobina', 'tags')),
        # ('Status da Bobina', ('tipo_bobina')),
    )
    class Meta:
        model = Bobina
        fields = [
            'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'tipo_bobina', 'tags'
        ]


class RequisicaoForm(NetBoxModelForm):
    class Meta:
        model = Requisicao
        fields = ('bilhete_associado',)

# Tem que fazer uma classe para 'FibraRequisitada'. Veja em: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step04-forms.md#accesslistruleform



# FilterSets

# Bobinas:

class BobinaFilterForm(NetBoxModelFilterSetForm):
    model = Bobina

    quantidade_fibras = forms.ModelMultipleChoiceField(
        queryset=Bobina.objects.all(),
        required=False
    )
    lote_cabo = forms.ModelMultipleChoiceField(
        queryset=Bobina.objects.all(),
        required=False
    )
    nome_fornecedor = forms.ModelMultipleChoiceField(
        queryset=Fornecedor.objects.all(),
        required=False
    )
