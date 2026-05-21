# Relatório do projeto S1_R3-AT2_LOPAL

Este projeto tem 11 scripts desenvolvidos em Python focados na resolução de problemas clássicos de lógica de programação. Os códigos exploram estruturas de repetição, validações de dados e manipulação de coleções como listas e dicionários, cada arquivo corresponde a um exercício diferente.

## Conteúdo dos arquivos

### `01 Atividade.py`
Mostra os números pares e ímpares de 0 a 100.
- Percorre `range(101)`.
- Verifica se `x % 2 == 0`.
- Imprime se o número é par ou ímpar.

### `02 Atividade.py`
Lê três números e informa o maior e o menor.
- Lê três inteiros via `input()`.
- Guarda em uma lista e usa `sort()` para deixar em ordem crescente.
- Mostra o primeiro e o último valor da lista ordenada.

### `03 Atividade.py`
Imprime o nome na vertical em forma de escada.
- Lê `nome` do usuário.
- Constrói a saída acumulando letras em uma string.
- Exibe um novo nível da escada a cada letra.

### `04 Atividade.py`
Gera a série de Fibonacci até o n-ésimo termo.
- Lê o valor `termo`.
- Usa `a, b = 1, 1` como primeiros elementos.
- Empilha os valores em uma lista com `while`.
- Atualiza `a, b = b, a + b` a cada interação.

### `05 Atividade.py`
Valida dados do usuário:
- Nome com mais de 3 caracteres.
- Idade entre 0 e 150.
- Salário maior que zero.
- Sexo como `f` ou `m`.
- Estado civil como `s`, `c`, `v` ou `d`.
- Usa `while` para repetir solicitações de entrada até que cada valor fique válido.

### `06 Atividade.py`
Verifica se um número inteiro é primo.
- Lê o número do usuário.
- Conta quantos divisores o número tem.
- Se o total de divisores for 2, é primo.

### `07 Atividade.py`
Calcula o fatorial de um número.
- Lê o número do usuário.
- Usa `for` decrescente de `numero` até 1.
- Multiplica sucessivamente os valores.
- Imprime a expressão da fatoração e o resultado.

### `08 Atividade.py`
Trabalha com uma lista fixa `[5, 7, 2, 9, 4, 1, 3]`.
- Mostra o tamanho com `len()`.
- Encontra maior e menor com `max()` e `min()`.
- Soma os valores com `sum()`.
- Ordena a lista em ordem crescente com `sort()` e decrescente com `reverse()`.

### `09 Atividade.py`
Cria e exibe uma tabela de preços usando dicionário.
- Define listas `produtos` e `precos` dentro de `tabela`.
- Usa `zip()` para combinar itens e imprimir cada par.

### `10 Atividade.py`
Valida uma senha usando `while`.
- Pede a senha até que o usuário digite `676767`.
- Exibe `Acesso liberado` quando a senha estiver correta.

### `11 Atividade.py`
Mostra a tabuada de um número de 1 a 10.
- Lê um número entre 1 e 10.
- Usa `for i in range(1, 11)` para imprimir a tabuada.

## Observações gerais
Os códigos exploram conceitos básicos de Python: laços de repetições, condicionais, listas, dicionários e entrada de usuário. O projeto serviu para fixar bem a base do Python. Deu para entender quando usar for ou while, como tratar o que o usuário digita para evitar erros e como organizar informações usando listas e dicionários.
