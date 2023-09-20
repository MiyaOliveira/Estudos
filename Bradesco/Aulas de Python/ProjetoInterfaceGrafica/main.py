class Pessoa:
    'Isso é uma classe nova chamada pessoa'

    idade = 15

    def saudacao(self):
        print('Olá Pessoas!')

# create a new object of person class
matheus = Pessoa()

# Output: 15
print(matheus.idade)

#Output: <bound method Person.greet of <__main__.Person object>>
print(matheus.saudacao)

# Output: 'isso é uma nova classe chamada pessoa'
print(Pessoa.__doc__)

# Chamando o método saudacao()
matheus.saudacao()