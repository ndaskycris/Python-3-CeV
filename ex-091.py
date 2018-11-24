from random import randint
from time import sleep
from operator import itemgetter
dicio = {'Jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in dicio.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print()
print('Ranking:')
# sort_dicio = [(v, k) for k, v in dicio.items()]
# sort_dicio.sort(reverse=True)
sort_dicio = sorted(dicio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(sort_dicio):
    print(f'{i + 1}º: {v[0]} com {v[1]}.')
    sleep(0.5)
