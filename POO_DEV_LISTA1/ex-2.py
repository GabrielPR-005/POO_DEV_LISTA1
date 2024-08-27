class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} feito!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} feito!")
        else:
            print("Saldo insuficiente ou valor de saque inválido!")

    def consultar_saldo(self):
        print(f"Saldo: R${self.__saldo:.2f}")

conta = ContaBancaria(10000)  # Inicializando a conta com um saldo 

conta.consultar_saldo()      # Consulta o saldo atual
conta.depositar(1500)         # Deposita 
conta.consultar_saldo()      # Consulta o saldo após o depósito
conta.sacar(1000)             # Saca 
conta.consultar_saldo()      # Consulta o saldo após o saque