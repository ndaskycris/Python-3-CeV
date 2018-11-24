from datetime import datetime
ano_pres = datetime.now().year
dicio = dict()
dicio['Nome'] = str(input('Nome: ')).strip().title()
while True:
    nasc = int(input('Ano de nascimento [AAAA]: '))
    if nasc < 1900:
        print('Digite ano de nascimento no formato AAAA.')
    else:
        break
dicio['Idade'] = ano_pres - nasc
dicio['CTPS'] = int(input('Número da CTPS [0 se não tiver]: '))
if dicio['CTPS'] != 0:
    while True:
        ano_cont = int(input('Ano de contratação [AAAA]: '))
        if ano_cont < 1900:
            print('Digite ano de contratação no formato AAAA')
        else:
            break
    dicio['Ano da contratação'] = ano_cont
    dicio['Salário'] = float(input('Salário: R$ '))
    dicio['Idade de aposentadoria'] = (ano_pres - nasc) + (35 - (ano_pres - ano_cont))
else:
    dicio['CTPS'] = 'Não possui'
print('-=' * 30)
print(dicio)
for k, v in dicio.items():
    if k == 'Idade' or k == 'Idade de aposentadoria':
        print(f'{k}: {v} anos')
    elif k == 'Salário':
        print(f'{k}: R$ {v}')
    else:
        print(f'{k}: {v}')
