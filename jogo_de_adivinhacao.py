import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

# Loop principal do jogo
while True:
    # Lê o palpite do jogador
    palpite = int(input("Digite o seu palpite: "))

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número é maior! Tente novamente.")
    else:
        print("O número é menor! Tente novamente.")
