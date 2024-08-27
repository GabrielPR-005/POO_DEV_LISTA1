class FormaGeometrica:
    def calcularArea():
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14*self.raio**2
    
circulo = Circulo(5)
quadrado = Quadrado(2)

print(f"Área quadrado = {quadrado.calcularArea()}")
print(f"Área círculo = {circulo.calcularArea()}")