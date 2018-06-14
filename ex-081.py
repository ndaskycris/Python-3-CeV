lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break

print('-' * 40)
if 5 in lista:
    print(f'O valor 5 foi digitado na {lista.index(5)}ª posição.')
else:
    print('O valor 5 não faz parte da lista!')
print(f'Você digitou {len(lista)} elementos.')
lista.sort()
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
