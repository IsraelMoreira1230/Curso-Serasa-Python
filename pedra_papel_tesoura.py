import random


class JogoPedraPapelTesoura:
    def jogar(self):
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        jogador = input("Escolha entre 'Pedra', 'Papel' ou 'Tesoura': ")
        jogador = jogador.capitalize()

        if jogador not in opcoes:
            print("Opção inválida. Escolha entre 'Pedra', 'Papel' ou 'Tesoura'.")
            return

        computador = random.choice(opcoes)

        print(f"Jogador: {jogador}.")
        print(f"Computador: {computador}.")

        if jogador == computador:
            print("Empate!")
        elif (jogador == 'Pedra' and computador == 'Tesoura') or \
                (jogador == 'Papel' and computador == 'Pedra') or \
                (jogador == 'Tesoura' and computador == 'Papel'):
            print("Jogador venceu!")
        else:
            print("Computador venceu!")
