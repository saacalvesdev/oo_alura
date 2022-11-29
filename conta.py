class Conta:
    def __init__ (self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print('O saldo do titular {} é R$ {}.'.format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        valor <= (valor_disponivel)

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} ultrapassou o limite'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod       
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


conta = Conta(7, 'Isaac Alves', 1000.00, 2000.00)
conta2 = Conta(8, 'Eren Yagger', 1000.00, 2000.00)
conta.extrato()
conta.depositar(100)
conta.extrato()
conta.sacar(50)
conta.extrato()
conta.transferir(200.00,conta2)
conta2.extrato()
conta.extrato()