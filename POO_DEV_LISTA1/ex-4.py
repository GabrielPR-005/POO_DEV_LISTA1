class Calculadora:
    def adicionar(self, *args):
        return sum(args)

    def subtrair(self, *args):
        if len(args) == 0:
            return 0
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado

    def multiplicar(self, *args):
        if len(args) == 0:
            return 1
        resultado = args[0]
        for num in args[1:]:
            resultado *= num
        return resultado

    def dividir(self, *args):
        if len(args) == 0:
            raise ValueError("Nenhum valor foi fornecido.")
        resultado = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida.")
            resultado /= num
        return resultado


calc = Calculadora()

print(calc.adicionar(10, 10, 10))  # 30

print(calc.subtrair(50, 30, 10))   # 10

print(calc.multiplicar(2, 2, 8))   # 32

print(calc.dividir(100, 2, 5))     # 10.0

