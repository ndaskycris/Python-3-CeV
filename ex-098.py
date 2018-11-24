from time import sleep


def decor():
    print('-=' * 30)


def contador(i, f, p):
    quebra = 0  # contador para quebrar a linha caso a contagem personalizada fique muito grande.
    # ajustando o passo personalizado, caso necessário:
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    if i > f and p > 0:
        p *= -1
    print(f'Contagem de {i} até {f} no passo {p}:')
    # para cada inteiro entre INÍCIO até (FIM+1 se FIM maior que INÍCIO senão FIM-1), no passo P:
    for num in range(i, (f + 1 if f > i else f - 1), p):
        print(f'{num} ', end='', flush=True)
        quebra += 1
        if quebra % 20 == 0:  # quebra a linha da contagem personalizada a cada 20 iterações.
            print()
        sleep(0.5)
    print()


decor()
contador(1, 10, 1)
decor()
contador(10, 0, 2)
decor()
print('CONTAGEM PERSONALIZADA')
ini = int(input('Início: '))
fin = int(input('Fim: '))
pas = int(input('Passo: '))
decor()
contador(ini, fin, pas)
decor()
print('--- FIM DO PROGRAMA ---')
