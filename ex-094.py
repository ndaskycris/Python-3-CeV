lista = []
lista_mulher = []
dicio = dict()
cont = somaid = media = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo.startswith('F'):
        lista_mulher.append(nome)
    idade = int(input('Idade: '))
    cont += 1
    somaid += idade
    dicio = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    lista.append(dicio.copy())
    dicio.clear()
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
media = somaid / cont
print(lista)
print("-=" * 30)
print(f'O grupo tem {cont} pessoas.')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres cadastradas foram:', end=' ')
for i in lista_mulher:
    print(f'{i}', end='; ')
print()
print(f'Lista das pessoas mais velhas que a média:')
for j in lista:
    if j['Idade'] > media:
        for k, v in j.items():
            print(f'{k} = {v};', end=' ')
        print()
print('*** FIM DO PROGRAMA ***')
