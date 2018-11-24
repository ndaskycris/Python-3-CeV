def area(l, c):
    a = l * c
    print(f'A área do terreno de {l}m x {c}m é de {a}m².')


def linha():
    print('-' * 30)


print('CONTROLE DE TERRENOS')
linha()
quant = int(input('Quantos terrenos quer calcular? '))
linha()
for c in range(quant):
    print(f'TERRENO {c + 1}:')
    larg = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    area(larg, comp)
    linha()
print('--- FIM DO PROGRAMA ---')
