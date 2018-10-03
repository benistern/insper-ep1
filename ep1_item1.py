#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:29:46 2018

@author: benistern
"""

import json
with open ('cardapio.json','r') as arquivo:
    texto = arquivo.read()
cardapio = json.loads(texto)


'''cardapio = {
    'jujuba': 10,
'pipoca gourmet': 60, 'suco de tomate': 15, 'água': 2.5,
}'''
comanda = {
    'água': 3,
    'jujuba': 5,
}
 

print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
escolha = int(input("Faça sua escolha: ")) 



if escolha == 0:
        print("Até mais")
    

while escolha != 0:
    
    #imprimir cardapio
    if escolha == 1:
        print("O cardápio possui os seguintes itens:")
        
        for e in cardapio:
            print('{0}: {1:.2f}R$'.format(e,cardapio[e]))
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
        escolha = int(input("Faça sua escolha: ")) 
    
    #adicionar item
    if escolha == 2: 
        produto = input("Nome do produto: ")
        
        if produto not in cardapio:
            print("O item {0} não está no cardápio".format(produto))
        
        else:
            quantidade = int(input("Quantidade a adicionar: "))
            
            if quantidade < 0:
            
                while quantidade < 0:
                    print("Não é possível adicionar quantidade não positiva")
                    quantidade = int(input("Quantidade a adicionar: "))

            comanda[produto] += quantidade
            print("Quantidade atual de {1}: {0}".format(comanda[produto],produto))
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
        escolha = int(input("Faça sua escolha: ")) 
    
    #remover item
    if escolha == 3:
        produto_rem = input("Nome do produto: ")
        
        if produto_rem not in comanda:
            print("O item {0} não está na comanda".format(produto_rem))
        
        else:
            quantidade_rem = int(input("Quantidade a remover: "))
            
            if quantidade_rem < 0:
                    
                while quantidade_rem < 0:
                    print("Não é possível remover quantidade não positiva")
                    quantidade_rem = int(input("Quantidade a remover: "))
                
            elif quantidade_rem > comanda[produto_rem]:
                
                while quantidade_rem > comanda[produto_rem]:
                    print("Não é possível remover mais do que a quantidade presente na comanda\nMáximo a ser removido: {0}".format(comanda[produto_rem]))
                    quantidade_rem = int(input("Quantidade a remover: "))
                    
                comanda[produto_rem] -= quantidade_rem
                print("Quantidade atual de {0}: {1}".format(produto_rem, comanda[produto_rem]))        
            '''if comanda[produto_rem] == 0:
                del comanda[produto_rem]
                print("Removendo {0} da comanda...".format(produto_rem))'''
                
            if quantidade_rem == comanda[produto_rem]:
                print("Quantidade atual de {0}: {1}".format(produto_rem, 0))
                del comanda[produto_rem]
                print("Removendo {0} da comanda...".format(produto_rem))
                
            
            
            
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
        escolha = int(input("Faça sua escolha: "))
        
    #imprimir comanda
    if escolha == 4:
        print("A comanda possui os seguintes itens:")
        
        for i in comanda:
            print('{0}: {1}'.format(i,comanda[i]))
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
        escolha = int(input("Faça sua escolha: "))
        
    #edicao de cardapio
    if escolha == 5:
        print("1 - adicionar item ao cardapio\n2 - remover item do cardapio\n3 - alterar preco de um item")
        escolha_2 = int(input("Faça sua escolha: "))
        
        if escolha_2 == 1:
            nome_item = input("Escreva o nome do item que sera adicionado: ")
            while nome_item in cardapio:
                print("este item ja esta no cardapio")
                nome_item = input("Escreva o nome do item que sera adicionado: ")
                
            valor_item = int(input("Escreva o preço do item que sera adicionado: "))
            
            while valor_item < 0:
                valor_item = int(input("Escreva o preço do item que sera adicionado: "))
            
            else:
                cardapio[nome_item] = valor_item
        
        
        if escolha_2 == 2:
            nome_rem = input("Escreva o item que deseja remover do cardapio: ")
            del cardapio[nome_rem]
        
        if escolha_2 == 3:
            item_alterado = input("Escreva um item para o seu valor ser alterado: ")
            while item_alterado not in cardapio:
                print("Este item nao esta no cardapio ainda")
                item_alterado = input("Escreva um item para o seu valor ser alterado: ")
            novo_valor = float(input("Escreva o novo valor do item: "))
            while novo_valor < 0:
                print("O item nao pode ter um valor negativo")
                novo_valor = float(input("Escreva o novo valor do item: "))
            
            cardapio[item_alterado] = novo_valor
            print("Valor do item {0} foi alterado para {1}R$".format(item_alterado, novo_valor))
            
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda\n5 - edição do cardapio")
        escolha = int(input("Faça sua escolha: "))
        
            
novo_cardapio = json.dumps(cardapio, sort_keys = True, indent = 4)
with open ('cardapio.json','w') as arquivo:
    arquivo.write(novo_cardapio)
   
                    
                    
                    
                    