lista = []
while True:
    num = int(input('Adicione um valor: '))
    if num not in lista:
            lista.append(num)
            print('Valor adicionado.')
    else:
        print('Valor duplicado, não vou adicionar.')
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
print('')
print(f'Você digitou os seguintes valores: {sorted(lista)}')
