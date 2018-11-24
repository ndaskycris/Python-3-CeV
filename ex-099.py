from time import sleep


def decor():
    print('-=' * 30)


def maior(* val):
    decor()
    cont = maior = 0
    if not val:
        print('Não foi digitado nenhum valor.')
    else:
        for num in val:
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
            if cont == 0:
                maior = num
            elif num > maior:
                maior = num
            cont += 1
        print()
        print(f'Foram informados {cont} números.')
        print(f'O maior número digitado foi {maior}.')


maior(2, 5, 4, 9, 1)
maior(85, 98, 20)
maior(8, 2)
maior()
decor()
print('--- FIM DO PROGRAMA ---')
