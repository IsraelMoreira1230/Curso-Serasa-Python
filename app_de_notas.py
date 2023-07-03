class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print("A nota precisa estar entre 0 e 10.")

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def exibir_status(self):
        media = self.calcular_media()
        if media >= 7:
            print(f"{self.nome} está aprovado(a) com média {media:.2f}.")
        elif media >= 4:
            print(f"{self.nome} está em recuperação com média {media:.2f}.")
        else:
            print(f"{self.nome} está reprovado(a) com média {media:.2f}.")


class AppNotas:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome):
        aluno = Aluno(nome)
        self.alunos.append(aluno)

    def adicionar_nota_aluno(self, nome, nota):
        aluno = self.buscar_aluno(nome)
        if aluno:
            aluno.adicionar_nota(nota)
        else:
            print(f"Aluno '{nome}' não encontrado.")

    def buscar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno
        return None

    def exibir_status_aluno(self, nome):
        aluno = self.buscar_aluno(nome)
        if aluno:
            aluno.exibir_status()
        else:
            print(f"Aluno '{nome}' não encontrado.")
