class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f'Depósito de R${valor:.2f}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f'Saque de R${valor:.2f}')
        else:
            print('Saldo insuficiente!')

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.append(
                f'Transferência de R${valor:.2f} para conta {destino.numero}')
        else:
            print('Saldo insuficiente para transferência!')

    def extrato(self):
        print(f'--- Extrato da conta {self.numero} ---')
        print(f'Titular: {self.titular.nome}')
        print(f'Número: {self.numero}')
        print(f'Saldo: R${self.saldo:.2f}')
        print('Histórico:')
        for item in self.historico:
            print(item)


# Criando clientes
cliente1 = Cliente('João', '123.456.789-00')
cliente2 = Cliente('Maria', '987.654.321-00')
cliente3 = Cliente('Pedro', '456.789.123-00')

# Criando contas
conta1 = Conta(cliente1, 1)
conta2 = Conta(cliente2, 2)
conta3 = Conta(cliente3, 3)

# Fazendo operações de depósito nas contas
conta1.depositar(100)
conta2.depositar(200)
conta3.depositar(300)

# Fazendo operações de saque nas contas
conta1.sacar(50)
conta2.sacar(100)
conta3.sacar(200)

# Transferindo dinheiro entre contas
conta1.transferir(conta2, 30)

# Imprimindo o extrato de uma conta
conta1.extrato()
