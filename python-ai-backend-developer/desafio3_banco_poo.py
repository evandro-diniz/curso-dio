from abc import ABC, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self, saldo, numero, agencia, cliente) -> None:
        self._saldo = saldo
        self._numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @abstractmethod
    def saldo():
        pass
    
    @abstractmethod
    def sacar(limite, LIMITE_SAQUES):
        print("\n=============== SAQUE ==============")
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n------------------------------------------")
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\n------------------------------------------")
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\n------------------------------------------")
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n------------------------------------------")
            print("Saque realizado com sucesso!")

        else:
            print("\n------------------------------------------")
            print("Operação falhou! O valor informado é inválido.")

        print("=======================================")
        return saldo, extrato, numero_saques

    @abstractmethod
    def depositar():
        print("\n=============== DEPÓSITO ==============")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"
            print("\n------------------------------------------")
            print("Depósito realizado com sucesso!")

        else:
            print("\n------------------------------------------")
            print("\nOperação falhou! O valor informado é inválido.")
        
        print("=======================================")
        return saldo, extrato

    @abstractmethod
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques) -> None:
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:def realizar_transacao():
        pass

    def adicionar_conta():
        pass\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Transacao():
    def valor(self):
        pass
    def registrar(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente():
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Historico():
    def __init__(self) -> None:
        self._trasacoes = []

    def transacoes(self):
        return self._trasacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
