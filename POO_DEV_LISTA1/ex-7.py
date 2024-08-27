class Motor:
    def __init__(self, potencia, tipo_cambio):
        self.potencia = potencia
        self.tipo_cambio = tipo_cambio
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Motor ligado!")
        else:
            print("O motor já está ligado!")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Motor desligado!")
        else:
            print("O motor já está desligado!")
    
    def info(self):
        print(f"Tipo de Câmbio: {self.tipo_cambio}, Potência: {self.potencia}, Ligado: {self.ligado}")

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def ligar_carro(self):
        print(f"Ligando o carro {self.marca} {self.modelo}...")
        self.motor.ligar()

    def desligar_carro(self):
        print(f"Desligando o carro {self.marca} {self.modelo}...")
        self.motor.desligar()
    
    def info_total(self):
        self.motor.info()
        print(f"Marca: {self.marca}, Modelo: {self.modelo}\n")


motor = Motor(100, "Manual")  
carro = Carro("Fiat", "Cronos", motor)

carro.ligar_carro()  
carro.desligar_carro()  
carro.info_total()
