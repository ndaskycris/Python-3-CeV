matriz = []
somapar = somaterc = maior = 0
for i in range(0, 3):
    linha = []  # a cada iteração cria uma nova lista "linha".
    for j in range(0, 3):  # a cada iteração adiciona valores a cada coluna da lista "linha".
        num = (int(input(f'Digite um valor para [{i}, {j}]: ')))
        linha.append(num)
        if num % 2 == 0:
            somapar += num
        if j == 2:
            somaterc += num
    matriz.append(linha)  # adiciona a linha inteira à lista "matriz".
print('-=' * 20)
for c in range(0, 3):
    for k in range(0, 3):
        print(f'[{matriz[c][k]}:^5]', end='')
    print('')
print('-=' * 20)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterc}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
