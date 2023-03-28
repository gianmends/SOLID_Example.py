from Conta_Bancaria import Banco

class ContaPoupanca(Banco):
    def __init__(self, nome, cpf, senha, saldo, taxa_rendimento):
        super().__init__(nome, cpf, senha, saldo)
        self.taxa_rendimento = taxa_rendimento

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do depósito não pode ser negativo ou nulo.")
        self.saldo += valor
        
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque não pode ser negativo ou nulo.")
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente.")
        
    def rendimento_ao_ano(self, valor):
        taxa_rendimento = 0.05
        rendimento = valor * taxa_rendimento
        return rendimento
    
    def get_taxa_rendimento(self):
        return self.taxa_rendimento
    
    def set_taxa_rendimento(self, taxa_rendimento):
        self.taxa_rendimento = taxa_rendimento

    def calcular_rendimento_extra(self, tempo_extra):
        if tempo_extra.endswith("s"):
            tempo_extra = int(tempo_extra[:-1])
        elif tempo_extra.endswith("m"):
            tempo_extra = int(tempo_extra[:-1]) * 60
        elif tempo_extra.endswith("h"):
            tempo_extra = int(tempo_extra[:-1]) * 3600
        elif tempo_extra.endswith("d"):
            tempo_extra = int(tempo_extra[:-1]) * 86400
        elif tempo_extra.endswith("M"):
            tempo_extra = int(tempo_extra[:-1]) * 2592000
        elif tempo_extra.endswith("y"):
            tempo_extra = int(tempo_extra[:-1]) * 31536000
        else:
            raise ValueError("Tempo inválido")
        
        novo_saldo = self.saldo * (1 + self.taxa_rendimento/100) ** (tempo_extra/31536000)
        return novo_saldo