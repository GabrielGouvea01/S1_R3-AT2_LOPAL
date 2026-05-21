# 01 - Faça um algoritmo usando o for para mostrar os números pares e impares de 0 a 100.

for x in range(101):
  if x % 2 == 0:
    print(f"O nuemro {x} é par")
  else:
    print(f"O numero {x} é Impar")