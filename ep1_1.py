#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:29:46 2018

@author: benistern
"""
cardapio = {
    'jujuba': 10,
'pipoca gourmet': 60, 'suco de tomate': 15, 'água': 2.5,
}
comanda = {
    'água': 3,
    'jujuba': 5,
}
 

print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda")
escolha = int(input("Faça sua escolha: ")) 



if escolha == 0:
        print("Até mais")
    

while escolha != 0:
    
    #imprimir cardapio
    if escolha == 1:
        print("O cardápio possui os seguintes itens:")
        
        for e in cardapio:
            print('{0}: {1:.2f}R$'.format(e,cardapio[e]))
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda")
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
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda")
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
                
            
            
            
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda")
        escolha = int(input("Faça sua escolha: "))
        
    #imprimir comanda
    if escolha == 4:
        print("A comanda possui os seguintes itens:")
        
        for i in comanda:
            print('{0}: {1}'.format(i,comanda[i]))
        
        print("Comanda eletrônica\n0 - sair\n1 - imprimir cardápio\n2 - adicionar item\n3 - remover item\n4 - imprimir comanda")
        escolha = int(input("Faça sua escolha: "))
            
            
            
                    
                    
                    
                    
                    
                    