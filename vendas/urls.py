from django.urls import path
from . import views

urlpatterns = [
    path("adicionar/", views.adicionar_vendas, name="adicionar_vendas"),
    path("listar/", views.listar_vendas, name="listar_vendas"),
]
