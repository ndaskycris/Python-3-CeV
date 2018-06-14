lista = []
aux = 0
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if not lista:
        lista.append(num)
        print('Adicionado ao fim da lista.')
    elif num > lista[-1]:
        lista.append(num)
        print('Adicionado ao fim da lista.')
    else:
        for p, v in enumerate(lista):
            if num <= v:
                lista.insert(p, num)
                print(f'Adicionado na posição {p} da lista.')
                break
print('')
print(lista)