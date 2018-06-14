expressao = str(input('Digite a expressão: '))
parenteses = list(filter(lambda x: x in '()', expressao))
validade = 'correta'
peso = 0
for p in parenteses:
    if p == '(':
        peso += 1
    else:
        peso -= 1
        if peso < 0:
            validade = 'errada'
if peso != 0:
    validade = 'errada'
print(f'Sua expressão está {validade}.')