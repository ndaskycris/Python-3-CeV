listona = []
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    listona.append([nome, [nota1, nota2], media])  # adiciona pessoas à "listona".
    opt = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opt.startswith('N'):
        break
listona.sort()  # coloca a lista de alunos em ordem alfabética.
print('=' * 40)
print(f'Nº. NOME {"MÉDIA":>31}')
print('=' * 40)
for c in range(0, len(listona)):
    print(f'{c + 1}  {str(listona[c][0]):<33} {(listona[c][2]):.1f}')
print('=' * 40)
while True:
    opt2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opt2 == 999:
        break
    elif opt2 not in range(1, len(listona) + 1):  # considera que usuário vai usar numeração partindo de 1.
        print('Escolha inválida')
    else:
        print(f'As notas de {listona[opt2 - 1][0]} são: {listona[opt2 - 1][1]}')
        print('-' * 40)
print('=' * 40)
print('FIM DO PROGRAMA')