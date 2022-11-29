class Conta:
    def __init__ (self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print('O saldo do titular {} é R$ {}.'.format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    

conta = Conta(7, 'Isaac Alves', 1000.00, 2000.00)
conta.extrato()
conta.depositar(100)
conta.extrato()
conta.sacar(50)
conta.extrato()