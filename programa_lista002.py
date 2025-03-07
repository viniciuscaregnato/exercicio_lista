"""
Programa: lista
Descrição: Escreva um programa que busque um determinado elemento em uma lista. Agora, conforme o Nelson fez.
Autor: Vinicius Garcia
Versão: 0.0.2
Data: 03/03/2025
"""

# Alocação de memória
lista = [1,5,-1,9]

contador = 0

Achou = False

# Entrada de dados
numero = int(input("Escreva o numero que deseje procurar: "))

# Processamento de dados
while contador < len(lista):
    if lista[contador] == numero:
        achou = True
        break #sai do while
    contador += 1 # significa que contador = contador + 1



# Saída de dados

if achou:
    print(f"o numero {numero} foi encontrado na posiçao {contador}.")
else:
    print("o numero nao foi encontrado.")
