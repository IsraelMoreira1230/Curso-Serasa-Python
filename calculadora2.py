def divisao(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
    return num1 / num2

distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo gasto: "))

velocidade = divisao(distancia, tempo)

if velocidade is not None:
    print(f"Velocidade: {velocidade}")
