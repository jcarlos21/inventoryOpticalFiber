from django.urls import path
from . import models, views

urlpatterns = (

    # Fornecedor
    path('fornecedor/', views.FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedor/add/', views.FornecedorEditView.as_view(), name='fornecedor_add'),
    path('fornecedor/<int:pk>/', views.FornecedorView.as_view(), name='fornecedor'),
    path('fornecedor/<int:pk>/edit/', views.FornecedorEditView.as_view(), name='fornecedor_edit'),
    path('fornecedor/<int:pk>/delete/', views.FornecedorDeleteView.as_view(), name='fornecedor_delete'),

    # TipoBobina
    path('tipo-bobina/', views.TipoBobinaListView.as_view(), name='tipobobina_list'),
    path('tipo-bobina/add/', views.TipoBobinaEditView.as_view(), name='tipobobina_add'),
    path('tipo-bobina/<int:pk>/', views.TipoBobinaView.as_view(), name='tipobobina'),
    path('tipo-bobina/<int:pk>/edit/', views.TipoBobinaEditView.as_view(), name='tipobobina_edit'),
    path('tipo-bobina/<int:pk>/delete/', views.TipoBobinaDeleteView.as_view(), name='tipobobina_delete'),
    
    # Bobina
    path('bobina/', views.BobinaListView.as_view(), name='bobina_list'),
    path('bobina/add/', views.BobinaEditView.as_view(), name='bobina_add'),
    path('bobina/<int:pk>/', views.BobinaView.as_view(), name='bobina'),
    path('bobina/<int:pk>/edit/', views.BobinaEditView.as_view(), name='bobina_edit'),
    path('bobina/<int:pk>/delete/', views.BobinaDeleteView.as_view(), name='bobina_delete'),

    # Requisicao
    path('requisicao/', views.RequisicaoListView.as_view(), name='requisicao_list'),
    path('requisicao/add/', views.RequisicaoEditView.as_view(), name='requisicao_add'),
    path('requisicao/<int:pk>/', views.RequisicaoView.as_view(), name='requisicao'),
    path('requisicao/<int:pk>/edit/', views.RequisicaoEditView.as_view(), name='requisicao_edit'),
    path('requisicao/<int:pk>/delete/', views.RequisicaoDeleteView.as_view(), name='requisicao_delete'),
)