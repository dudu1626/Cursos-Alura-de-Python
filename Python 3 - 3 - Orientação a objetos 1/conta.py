# criação de uma classe conta, como boa prática usa-se primeira letra em maiúscula

class Conta:

    # Modelo do objeto
    def __init__(self, numero, titular, saldo, limite):  # difinição das características da classe
        print("Construindo objeto...{}".format(self))
        #Atributos da classe
        self.__numero = numero # __nome do atributo faz com que eles fiquem privados, dificultandoo acesso direto
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos da classe
    def saldo(self): # criação das funções referentes à classe
        print("Sr. {}, O saldo da conta é R$ {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # método privado
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo Insuficiente!")

    def transferir(self, valor, cta_destino):
        if valor < self.__saldo:
            self.sacar(valor)
            cta_destino.depositar(valor)

    @property
    def saldo(self): # como boa prática, usar o nome "get" para métodos que pegam informações
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self): # funciona igual ao método com o nome "get", mas não se usa como função , ou seja sem ()
        return self.__limite

    @limite.setter
    def limite(self, limite): # artifício para mudar o valor diretamente sem aparentar uma função
        self.__limite = limite

    @staticmethod #método estático da classe, no caso desse ser o sistema do banco código 001, ou seja nunca muda
    def codigo_bco():
        return "001"