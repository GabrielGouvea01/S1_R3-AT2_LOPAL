#04 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

termo = int(input("Até qual termo você quer gerar? "))
a, b = 1, 1

ordem = []
if termo < 0:
    print("0 não da")
elif termo == 1:
    print("Série de Fibonacci até o 1º termo: [1]")
else:
    count = 0
    while count < termo:
        ordem.append(a)
        a, b = b, a + b
        count += 1
    print(f"Série de Fibonacci até o {termo}º termo:")
    print(ordem)