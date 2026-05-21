# 03 - Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada.

nome = input("Fale o seu nome: ")
espaço = ""

for letra in nome:
  espaço = espaço + letra
  print(espaço)