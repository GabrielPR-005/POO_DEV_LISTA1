class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Nota: {self.nota}")

class Escola:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno(a) {aluno.nome} adicionado(a)!")

    def exibir_alunos(self):
        print("Lista de Alunos:")
        for aluno in self.alunos:
            aluno.info()
            print()  

escola = Escola()

aluno_1 = Aluno("Julia Jobim", "99999", 10.0)
aluno_2 = Aluno("Gabriel Ribeiro", "00001", 9.7)
aluno_3 = Aluno("Eduarda Pinheiro", "62341", 9.0)

escola.adicionar_aluno(aluno_1)
escola.adicionar_aluno(aluno_2)
escola.adicionar_aluno(aluno_3)

escola.exibir_alunos()
