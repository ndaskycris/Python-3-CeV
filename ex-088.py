from random import randint
from time import sleep
print('-' * 31)
print(f'{"JOGA NA MEGA SENA":^31}')
print('-' * 31)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quant} {"JOGOS" if quant > 1 else "JOGO"}', '-=' * 3)
jogos = []  # cria a lista "jogos".
for c in range(quant):
    palp = []  # a cada iteração cria uma nova lista vazia de palpites.
    while len(palp) < 6:  # adiciona 6 valores diferentes na lista de palpites.
        num = randint(1, 60)
        if num not in palp:
            palp.append(num)
    palp.sort()
    jogos.append(palp[:])  # adiciona a cópia da lista de palpites à lista "jogos".
    print(f'Jogo {c + 1}:{str(jogos[c]):>25}')
    sleep(1)
print('-=' * 4, '< BOA SORTE >', '-=' * 4)
