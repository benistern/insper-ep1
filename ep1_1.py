#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:29:03 2018

@author: benistern
"""

cardapio = {
    'jujuba': 10,
'pipoca gourmet': 60, 'suco de tomate': 15, 'água': 2.5,
}
comanda = {
    'água': 3,
    'jujuba': 1,
}
 

print("Comanda eletrônica/n0 - sair/n1 - imprimir cardápio/n2 - adicionar ite/n3 - remover item/n4 - imprimir comanda")
escolha = input("Faça sua escolha: ") 

#escolha = 0
if escolha == 0:
	print("Até mais")

while escolha != '0':
    #imprimir cardapio
    if escolha == 1:
        print("O cardápio possui os seguintes itens:")
        for e in cardapio:
            print('{0}: {1}R$'.format(e,cardapio[e]))
    #adicionar item
    if escolha == 2:
        produto = input("Nome do produto: ")
        if produto not in cardapio:
            print("O item {0} não está no cardápio".format(produto))
        else:
            quantidade = int(input("Quantidade a adicionar: "))
            if quantidade < 0:
                print("Não é possível adicionar quantidade não positiva")
            else:
                comanda[produto] += quantidade
                print("Quantidade atual de pipoca gourmet: {0}".format(comanda[produto]))
    #remover item
    if escolha == 3:
        produto_rem = input("Nome do produto: ")
        if produto_rem not in comanda:
            print("O item {0} não está na comanda".format(produto_rem))
        else:
            quantidade_rem = int(input("Quantidade a remover: "))
            if quantidade_rem < 0:
                print("Não é possível remover quantidade não positiva")
            elif quantidade_rem > comanda[produto_rem]:
                
        
        
            
























