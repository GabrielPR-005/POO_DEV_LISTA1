from abc import ABC

class Conta_Banc(ABC):

    def __init__(self, saldo, titular):
        self.__saldo = saldo  # atributo privado
        self.__titular = titular  # atributo privado

    def calcularRend(self, temp_Meses):
        return ((1 + self.tx_rend) ** temp_Meses) * self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

class Conta_Cor(Conta_Banc):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
        self.tx_rend = 0  # Taxa de rendimento da Conta Corrente é 0

class Conta_Poup(Conta_Banc):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
        self.tx_rend = 0.01  # Taxa de rendimento da Poupança

class Conta_Invest(Conta_Banc):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
        self.tx_rend = 0.02  # Taxa de rendimento da Conta Investimento


def __main__():
    c1 = Conta_Cor(2000, "Luis")
    c2 = Conta_Poup(2000, "João")
    c3 = Conta_Invest(2000, "Mariano")

    lista_contas = [c1, c2, c3]
    for conta in lista_contas:
        print(f"Titular: {conta.get_titular()}, Saldo após rendimento: {conta.calcularRend(3)}")
    
    
    c1.depositar(500)
    print(f"Saldo de {c1.get_titular()} após depósito: {c1.get_saldo()}")

    c1.sacar(1000)
    print(f"Saldo de {c1.get_titular()} após saque: {c1.get_saldo()}")

if __name__ == '__main__':
    __main__()
