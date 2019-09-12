class Conta:
    numero_conta = 0
    nome_correntista = ''
    saldo = 0

    def get_dados(self):
        msg = "N/C: " + str(self.numero_conta) + "\n" + "Titular: " + self.nome_correntista + "\n" + "Saldo: " + str(self.saldo)
        return msg