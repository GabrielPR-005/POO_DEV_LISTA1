class Animal:
    def emitirSom(self):
        return "Som Animalesco"

class Cachorro(Animal):
    def emitirSom(self):
        return "AUAUAU"

class Gato(Animal):
    def emitirSom(self):
        return "MIAUMIAU"

animal = Animal()
cachorro = Cachorro()
gato = Gato()

print("Animal:", animal.emitirSom())  
print("Cachorro:", cachorro.emitirSom()) 
print("Gato:", gato.emitirSom())