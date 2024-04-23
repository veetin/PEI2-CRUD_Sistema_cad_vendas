from django.db import models


# Create your models here.
class Vendas(models.Model):
    nome_cliente = models.CharField(
        verbose_name="Nome do Cliente", max_length=255, null=False, blank=False
    )
    cpf_cliente = models.IntegerField(
        verbose_name="CPF do Cliente"
    )
    telefone_cliente = models.IntegerField(
        verbose_name="Telefone do Cliente"
    )
    nome_produto = models.CharField(
        verbose_name="Nome do Produto", max_length=255, null=False, blank=False
    )
    preco_produto = models.FloatField(
        verbose_name="Preço", max_length=10, null=False, blank=False
    )
    situação_produto = models.IntegerField(
        verbose_name="Situação", null=False, blank=False
    )
    observacao = models.TextField()
    data_venda = models.DateTimeField(
        verbose_name="Data de venda", auto_now_add=True, null=False, blank=False
    )
