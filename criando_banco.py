class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Historico:
    def __init__(self):
        self.movimentacoes = []

    def registrar_movimentacao(self, movimentacao):
        self.movimentacoes.append(movimentacao)

    def exibir_movimentacoes(self):
        for movimentacao in self.movimentacoes:
            print(movimentacao)


class Conta:
    def __init__(self, numero, titular, saldo, limite, depositos):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.depositos = depositos
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.depositos += 1
        self.historico.registrar_movimentacao(f"Depósito de R$ {valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.registrar_movimentacao(f"Saque de R$ {valor}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.registrar_movimentacao(
                f"Transferência de R$ {valor} para a conta {conta_destino.numero}")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo: R$ {self.saldo}")

    def exibir_historico(self):
        self.historico.exibir_movimentacoes()
