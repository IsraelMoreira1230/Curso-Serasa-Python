import random

numero_secreto = random.randint(1, 100)
total_pontos = 1000

print("Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

nivel = input("Escolha o nível de dificuldade (Fácil, Médio ou Difícil): ")

# Define o número máximo de tentativas com base no nível de dificuldade
if nivel.lower() == "fácil":
    max_tentativas = 20
elif nivel.lower() == "médio":
    max_tentativas = 10
else:
    max_tentativas = 5

# Loop principal do jogo
for tentativa in range(1, max_tentativas+1):
    print(f"Tentativa {tentativa}")

    palpite = int(input("Digite o seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        print(f"Total de pontos: {total_pontos}")
        break
    else:
        pontos_perdidos = abs(numero_secreto - palpite)
        total_pontos -= pontos_perdidos
        if tentativa == max_tentativas:
            print("Suas tentativas acabaram!")
            print(f"O número secreto era: {numero_secreto}")
            print(f"Total de pontos: {total_pontos}")
        else:
            if palpite < numero_secreto:
                print("O número é maior! Tente novamente.")
            else:
                print("O número é menor! Tente novamente.")
