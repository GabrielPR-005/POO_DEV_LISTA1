class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

pessoa1 = Pessoa("Julia", 19)
pessoa1.informacoes()
