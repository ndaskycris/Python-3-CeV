lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número na Posição {cont}: ')))
print('=-' * 20 + '=')
print(f'Você digitou os valores {lista}.')
print(f'O maior número digitado foi {max(lista)} nas posições', end=' ')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}...', end=' ')
print(f'\nO menor número digitado foi {min(lista)} nas posições', end=' ')
for posi, c in enumerate(lista):
    if c == min(lista):
        print(f'{posi}...', end=' ')
