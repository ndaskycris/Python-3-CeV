from time import sleep
from random import randint



def sorteio(lista):
    print('Sorteando 5 valores... ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[c]} ', end='', flush=True)
        sleep(0.5)
    print()


def somapar(lista):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares sorteados é igual a {soma}')

numeros = []
sorteio(numeros)
somapar(numeros)
