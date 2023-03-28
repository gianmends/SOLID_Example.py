from Conta_Bancaria import Banco

class Conta(Banco):
    def __init__(self, nome, cpf, senha, saldo):
        super().__init__(nome, cpf, senha, saldo)

    def nome(self):
        return super().nome
 
    def nome(self, value):
        super().nome = value
 
    def cpf(self):
        return super().cpf
 
    def cpf(self, value):
        super().cpf = value
    
    def senha(self):
        return super().senha
    
    def senha(self, value):
        super().senha = value
    
    def saldo(self):
        return super().saldo
    
    def saldo(self, value):
        super().saldo = value

class GerenciadorDeContas:
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, nome, cpf, senha):
        nova_conta = Conta(nome, cpf, senha, 0)
        self.contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")

    def verificar_conta(self, cpf, senha):
        for conta in self.contas:
            if conta.cpf == cpf and conta.senha == senha:
                return conta
        return None