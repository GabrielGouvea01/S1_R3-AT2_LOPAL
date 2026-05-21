# 11 - Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.

num = int(input("Digite um número de 1 a 10: "))

print(f"Tabuada do {num}")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")