class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade em estoque: {self.quantidade}")

produto_1 = Produto("Caixa de Chocolate", 20.00, 100)
produto_2 = Produto("Pudim", 50.00, 40)
produto_3 = Produto("Palha Italiana", 8.00, 250)
produto_4 = Produto("Barra de Chocolate", 10.00, 150)

produto_1.info()
print() # ESSE PRINT SERVE COMO LINHA EM BRANCO PARA SEPARAR NA HORA DE PRINTAR
produto_2.info()
print()
produto_3.info()
print()
produto_4.info()
