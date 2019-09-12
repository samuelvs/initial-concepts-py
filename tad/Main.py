from Conta import *

c1 = Conta()
c2 = Conta()
c3 = Conta()

c1.numero_conta = 1
c1.nome_correntista = "Samuel Veloso"
c1.saldo = 100

c2.numero_conta = 2
c2.nome_correntista = "Maria do Santos"
c2.saldo = 90

c3.numero_conta = 3
c3.nome_correntista = "Pedro Junior"
c3.saldo = 200

contas = []
contas.append(c1)
contas.append(c2)
contas.append(c3)

conta_ms = Conta()
print("Contas no sistema:")
for i in contas:
    if i.saldo > conta_ms.saldo:
        conta_ms = i
    print(i.get_dados())

print("Maior saldo no sistema:" + conta_ms.get_dados())
