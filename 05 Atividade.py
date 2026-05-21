# #05 - Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Me fale seu nome: ")

while len(nome) <= 3:
  nome = input("Seu nome é muito curto, digite novamente: ")
  nome = nome.title()

##
idade = int(input("Fale sua idade: "))
while idade > 0 and idade > 150:
  idade = int(input("Sua idade esta acima ou abaixo do esperado, digite novamente:"))

##
salario = float(input("Fale o seu salario: "))

while salario <= 1:
  salario = float(input("Salario muito pequeno, digite novamente: "))

##
sexo = input("Qual é o seu genero, Digite 'f' para feminino e 'm' para masculino: ")
sexo = sexo.lower()

while sexo != "f" and sexo != "m":
  sexo = input("Voce digitou errado, escrea 'f' para feminino e 'm' para masculino: ")
  sexo = sexo.lower()

##
estado_civil = input("Escreva seu estado civil,por exemplo: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado: ")
estado_civil = estado_civil.lower()

while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Escreva seu estado civil novamente, por exemplo: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado: ")
    estado_civil = estado_civil.lower()

print("\n")
print("-"*40)
print("Verifique se as informaçoes estao corretas, se caso não esteja certo as suas informações, refaça o seu cadastro:")
print(f"Seu nome: {nome}")
print(f"Sua idade: {idade}")
print(f"Seu salário: {salario}")
print(f"Seu sexo: {sexo}")
print(f"Seu estado civil: {estado_civil}")
