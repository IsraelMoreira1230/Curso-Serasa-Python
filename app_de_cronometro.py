import time


class Cronometro:
    def __init__(self):
        self.inicio = 0
        self.fim = 0

    def iniciar(self):
        self.inicio = time.time()
        print("Cronômetro iniciado.")

    def parar(self):
        if self.inicio == 0:
            print("O cronômetro ainda não foi iniciado.")
        else:
            self.fim = time.time()
            print("Cronômetro parado.")

    def reiniciar(self):
        self.inicio = 0
        self.fim = 0
        print("Cronômetro reiniciado.")

    def exibir_tempo_decorrido(self):
        if self.inicio == 0:
            print("O cronômetro ainda não foi iniciado ou já foi reiniciado.")
        elif self.fim == 0:
            print("O cronômetro está em execução.")
        else:
            tempo_decorrido = self.fim - self.inicio
            print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos.")
