class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, multimidia, tipo_cambio):
        super().__init__(marca, modelo)
        self.multimidia = multimidia
        self.tipo_cambio = tipo_cambio
    
    def info_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Possui Multimídia: {self.multimidia}")
        print(f"Tipo de Câmbio: {self.tipo_cambio}")


carro_1 = Carro("Chevrolet", "Cruze", "Sim", "Automático")
carro_1.info_carro()

print()

carro_2 = Carro("Fiat", "Cronos", "Não", "Manual")
carro_2.info_carro()