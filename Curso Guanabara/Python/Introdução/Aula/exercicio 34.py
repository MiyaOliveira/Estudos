s = int(input('digite seu salario para calcular o ajuste:'))

if s <= 1250:
    ajuste = s * 1.15
    print('seu salario com o ajuste sera de R${}'.format(ajuste))
elif s > 1250:
    ajuste = s * 1.10
    print('seu salario com o ajuste sera de R${}'.format(ajuste))
else:
    print('digite um favor valido, por favor')