"""
Programa: lista
Descrição: Escreva um programa que busque um determinado elemento em uma lista. Considere inicialmente a lista [1,5,-1,9]
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""

# Alocação de memória
lista = [1,5,-1,9]

# Entrada de dados
numero = int(input("Escreva o numero que deseje procurar: "))

# Processamento e saída de dados
if numero in lista:
    print("seu numero está na lista")
else:
    print("seu numero nao esta na lista")


