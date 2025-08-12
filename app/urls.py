from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo-dominio', views.novo_dominio, name='novo_dominio'),
    path('novo-cliente', views.novo_dominio, name='novo_cliente'),
    path('editar-dominio', views.editar_dominio, name='editar_dominio'),
    path('editar-cliente', views.editar_cliente, name='editar_cliente'),
]
