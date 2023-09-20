arquivo = open('ponto.txt', 'w')
arquivo.write('eu amo python')
arquivo.close()

leitura = open('ponto.txt', 'r')
print(leitura.read())
leitura.close()