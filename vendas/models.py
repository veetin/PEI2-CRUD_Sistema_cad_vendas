from django.db import models


# Create your models here.
class Vendas(models.Model):
    nome_cliente = models.CharField(
        verbose_name="Nome do Cliente", max_length=255, null=False, blank=False
    )
    cpf_cliente = models.CharField(
        verbose_name="CPF do Cliente",
        max_length=11

    )
    telefone_cliente = models.CharField(
        verbose_name="Telefone do Cliente",
        max_length=11
    )
    nome_produto = models.CharField(
        verbose_name="Nome do Produto", max_length=255, null=False, blank=False
    )
    preco_produto = models.CharField(
        verbose_name="Preço", max_length=10, null=False, blank=False
    )
    situacao_produto = models.IntegerField(
        verbose_name="Situação", default=1 ,null=False, blank=False
    )
    observacao = models.TextField()
    data_venda = models.DateTimeField(
        verbose_name="Data de venda", auto_now_add=True, null=False, blank=False
    )

    def __str__(self) -> str:
        return self.nome_cliente
