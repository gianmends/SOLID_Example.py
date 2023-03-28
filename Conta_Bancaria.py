from abc import ABC, abstractmethod

class Banco(ABC):
    def __init__(self, nome, cpf, senha, saldo):
        self._nome: str = nome
        self._cpf: int = cpf
        self._senha: int = senha
        self._saldo: float = saldo

    def nome(self):
        return self._nome

    def nome(self, value):
        self._nome = value

    def cpf(self):
        return self._cpf

    def cpf(self, value):
        self._cpf = value

    def senha(self):
        return self._senha

    def senha(self, value):
        self._senha = value

    def saldo(self):
        return self._saldo
 
    def saldo(self, value):
        self._saldo = value
    
    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass