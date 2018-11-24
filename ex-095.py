listona = []
dicio = dict()
while True:
    dicio.clear()
    lista_gols = []
    nome = str(input('Nome do jogador: ')).strip().title()
    quant = int(input('Participou de quantos jogos? '))
    for c in range(quant):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        lista_gols.append(gols)
    dicio = {'Nome': nome, 'Gols': lista_gols, 'Soma': sum(lista_gols)}
    listona.append(dicio.copy())
    opt = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
print('-=' * 30)
print('Cod ', end='')
for item in dicio.keys():
    print(f'{item:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(listona):  # para cada valor V na chave K dentro da LISTONA, faça:
    print(f'{k:<3}', end='')  # printar número da chave K, sem pular linha, com espaço de 3 caracteres.
    for d in v.values():  # para cada dado D dentro do valor de dicionário V, faça:
        print(f'{str(d):<15}', end='')  # printar dado D, como string, sem pular linha, com espaço de 15 caracteres.
    print()
print('-' * 40)
while True:
    opt2 = int(input('Mostrar dados de qual jogador (999 para sair)? '))
    print('-' * 30)
    if opt2 >= 999:
        print('FIM DO PROGRAMA!')
        break
    if opt2 not in range(len(listona)):
        print('Código inválido, tente novamente.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {listona[opt2]["Nome"]}')
        # para cada valor G na chave I dentro da lista de gols dentro do dicionário dentro da listona, faça:
        for i, g in enumerate(listona[opt2]['Gols']):
            print(f'No jogo {i + 1} fez {g} {"gols" if g > 1 else "gol"}.')  # printar número de gols.
        print('-' * 30)
print('-=' * 30)
