# 02 - Escreva um script que leia três números e mostre o maior e o menor deles. Use Lista.

n1 = int(input("Fale o primeiro numero: "))
n2 = int(input("Fale o segundo numero: "))
n3 = int(input("Fale o terceiro numero: "))

lista = [n1,n2,n3]
lista.sort()
print(f"O menor numero é {lista[0]} e o maior é {lista[2]}")