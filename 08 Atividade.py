# 08 - Dada a lista
# L = [5, 7, 2, 9, 4, 1, 3]
# Escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]
print(lista)

tamanho = len(lista)
print(f"O tamanho da sua lista é: {tamanho}")

maior = max(lista)
menor = min(lista)
print(f"O seu maior número é: {maior}")
print(f"O seu menor número é: {menor}")

soma = sum(lista)
print(f"A soma da sua lista é: {soma}")

lista.sort()
print(f"Sua lista fica de forma crescente: {lista}")

lista.reverse()
print(f"Sua lista fica de forma decrescente: {lista}")