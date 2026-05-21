# 10 - Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente. A senha devera ser a seguinte senha númerica : "676767".

senha = int(input("Digite a senha: "))

while senha != 676767:
    print("Senha incorreta, tente novamente.")
    senha = int(input("Digite a senha: "))
if senha == 676767:
    print("Acesso liberado")
