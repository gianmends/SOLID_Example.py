from Conta_Bancaria import Banco

class ContaCorrente(Banco):
    def __init__(self, nome, cpf, senha, saldo, limite_saque, limite, banco: Banco):
        super().__init__(nome, cpf, senha, saldo)
        self.limite_saque: float = limite_saque
        self.limite: float = limite
        self.banco: Banco = banco
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do depósito não pode ser negativo ou nulo.")
        self.saldo += valor
    
    def sacar(self, valor):
        if self.banco.saldo + self.limite >= valor:
            self.banco.sacar(valor)
        else:
            raise ValueError("Limite de saque excedido!")
    
    def get_limite_saque(self):
        return self.limite_saque
    
    def set_limite_saque(self, limite_saque):
        self.limite_saque = limite_saque
        
    def get_limite(self):
        return self.limite
    
    def set_limite(self, limite):
        self.limite = limite