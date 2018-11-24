princ = []
temp = []
maior = menor = 0
while True:  # adicionando nomes e pesos à lista "dados", que depois será adicionada à lista "pessoas".
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:  # definindo maior e menor caso só haja uma pessoa na lista.
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
print(f'Foram cadastradas {len(princ)} {"pessoa" if len(princ) <= 1 else "pessoas"}.')
print(f'O menor peso cadastrado foi {menor}Kg. Peso de ', end='')
for c in princ:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')
print()
print(f'O maior peso cadastrado foi {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
