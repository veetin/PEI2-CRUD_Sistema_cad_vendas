from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vendas
from django.core.paginator import Paginator

def adicionar_vendas(request):
    if request.method == "GET":
        return render(request, "adicionar_vendas.html")
    elif request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        cpf_cliente = request.POST.get('cpf')
        telefone_cliente = request.POST.get('telefone')
        nome_produto = request.POST.get('nome_produto')
        preco_produto = request.POST.get('preco_produto')
        situacao_produto = request.POST.get('situacao')
        observacao = request.POST.get('observacao')
    
        dados_vendas = Vendas(
            nome_cliente = nome_cliente,
            cpf_cliente = cpf_cliente,
            telefone_cliente = telefone_cliente,
            nome_produto = nome_produto,
            preco_produto = preco_produto,
            situacao_produto = situacao_produto,
            observacao = observacao,
        )
       
        dados_vendas.save()

    return redirect("/vendas/adicionar")


def listar_vendas(request):
    if request.method == 'GET':
        vendas = Vendas.objects.all()

        cliente_filtrar = request.GET.get('filtro_cliente')

        situacao_filtrar = request.GET.get('filtro_situacao_produto')
        
        if cliente_filtrar:
            vendas = vendas.filter(nome_cliente__icontains=cliente_filtrar)
        if(situacao_filtrar):
            vendas = vendas.filter(situacao_produto__in=situacao_filtrar)

        venda_paginator = Paginator(vendas, 3)
        page_num = request.GET.get('page')
        page = venda_paginator.get_page(page_num)

        return render(request, "listar_vendas.html", {"page": page, "cliente_filtro": cliente_filtrar, "situacao_filtro": situacao_filtrar})
    
