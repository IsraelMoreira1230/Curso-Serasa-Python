def jogar_forca(palavra_secreta):
    tentativas = 6
    letras_corretas = []
    palavra_mascarada = "_" * len(palavra_secreta)

    print("Jogo da Forca")
    print("A palavra possui", len(palavra_secreta), "letras.")

    while tentativas > 0:
        print("Tentativas restantes:", tentativas)
        print("Palavra:", palavra_mascarada)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já acertou essa letra!")
        elif letra in palavra_secreta:
            letras_corretas.append(letra)
            nova_mascarada = ""
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    nova_mascarada += letra
                else:
                    nova_mascarada += palavra_mascarada[i]
            palavra_mascarada = nova_mascarada
            if palavra_mascarada == palavra_secreta:
                break
        else:
            tentativas -= 1
            print("Letra errada! Tente novamente.")

    if tentativas > 0:
        print("Parabéns, você acertou a palavra:", palavra_secreta)
    else:
        print("Suas tentativas acabaram. A palavra era:", palavra_secreta)


palavra_secreta = "python"
jogar_forca(palavra_secreta)
