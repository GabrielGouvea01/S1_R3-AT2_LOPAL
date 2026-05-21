# 06 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

numero = int(input("Digite um número: "))
div = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        div += 1
if div == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")