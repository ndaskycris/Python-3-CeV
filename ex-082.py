lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
res = list(filter(lambda x: x % 2 == 0, lista))
res2 = list(filter(lambda x: x % 2 == 1, lista))
print('')
print(f'Foram digitados os números: {lista}')
print(f'A lista de pares é {res}')
print(f'A lista de ímpares é {res2}')
