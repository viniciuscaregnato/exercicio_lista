"""
Programa: lista
Descrição: Escreva um programa que busque um determinado elemento em uma lista. Agora, com o comando FOR
Autor: Vinicius Garcia
Versão: 0.0.3
Data: 03/03/2025
"""

# Alocação de memória
lista = [1,5,-1,9]

contador = 0

achou = False

# Entrada de dados
numero = int(input("Escreva o numero que deseje procurar: "))

# Processamento de dados
for i in lista:
    if i == numero:
        achou = True
        ind = lista.index(numero)
        break

# Saída de dados

if achou:
    print(f"o numero {numero} foi encontrado na posiçao {ind}.")
else:
    print("o numero nao foi encontrado.")
