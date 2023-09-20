class main:
    pass

from Cliente import Cliente

from Conta  import Conta

c1 = Cliente('Pedro', '67998825087')
conta = Conta(c1._nome, 7865, 100)

conta.deposita(100)
conta.saque(50)
conta.extrato()