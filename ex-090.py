nome = str(input('Nome: ')).strip().title()
media = float(input(f'Média de {nome}: '))
if media >= 7.0:
    sit = 'APROVADO'
else:
    sit = 'REPROVADO'
dicio = {'Nome': nome, 'Média': media, 'Situação': sit}
for k, v in dicio.items():
    print(f'{k} é {v}')
