nome = str(input('Nome do jogador: ')).strip().title()
quant = int(input(f'Quantas partidas {nome} jogou? '))
lista = []
somagol = 0
for c in range(quant):
    gols = int(input(f'Quantos gols na partida {c + 1}? '))
    somagol += gols
    lista.append(gols)
dicio = {'Nome': nome, 'Gols': lista, 'Total': somagol}
print('-=' * 30)
print(dicio)
print('-=' * 30)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dicio["Nome"]} atuou em {quant} partidas.')
for i in range(quant):
    print(f'    => Na partida {i + 1}, fez {lista[i]} gols.')
print(f'Foi um total de {dicio["Total"]} gols.')
