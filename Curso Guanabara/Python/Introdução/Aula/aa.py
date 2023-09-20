print('para saber se suas retas formam um triangulo')
r1 = int(input('digite o valor de uma reta'))
r2 = int(input('digite o valor de outra reta'))
r3 = int(input('digite o valor da ultima reta'))

if r1 > r2:
    if r1 > r3:
        if r2 + r3 > r1:
            print('suas retas podem formar um triangulo')
        else:
            print('suas retas nao podem formar um triangulo')
    elif r1 < r3:
        if r1 + r2 > r3:
            print('suas retas podem formar um triangulo')
        else:
            print('suas retas nao podem formar um triangulo')
    else:
        print('suas retas nao podem formar um triangulo')
elif r1 < r2:
    if r2 > r3:
        if r1 + r3 > r2:
            print('suas retas podem formar um triangulo')
        else:
            print('suas retas nao podem formar um triangulo')
else:
    print('3 retas do mesmo tamanho nao podem formar um triangulo')


