class CalculadoraGorjeta:
    def calcular_gorjeta(self, total_conta, taxa_gorjeta):
        gorjeta = total_conta * (taxa_gorjeta / 100)
        total_pago = total_conta + gorjeta
        return gorjeta, total_pago

calculadora = CalculadoraGorjeta()

total_conta = float(input("Digite o valor total da conta: R$ "))
taxa_gorjeta = float(input("Digite a taxa de gorjeta (%): "))

gorjeta, total_pago = calculadora.calcular_gorjeta(total_conta, taxa_gorjeta)

print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total pago (incluindo gorjeta): R$ {total_pago:.2f}")
