import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar(saldo, extrato):
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



def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
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


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Ainda não foram realizadas movimentações." if not extrato else extrato)
    print("\n------------------------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==========================================")

def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        else:
            return None 

def novo_usuario(usuarios):
    print("\n================ USUÁRIOS ================")
    cpf = input("\nDigite seu cpf: ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario == None:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("Digite seu endereço: ")

        usuarios.append({
            "cpf":cpf, 
            "nome":nome, 
            "data_nascimento":data_nascimento,
            "endereco":endereco})
        print("\n------------------------------------------")
        print("Usuário cadastrado com sucesso")
        print("==========================================")
    else:
        print("\n------------------------------------------")
        print("Já existe um usuário com este CPF.")
        print("==========================================")
        return
    
def nova_conta(AGENCIA, usuarios, contas, numero_conta):
    print("\n================ CONTAS ================")
    cpf = input("\nDigite seu cpf: ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario == None:
        print("\n------------------------------------------")
        print("Usuário não existe.")
        print("==========================================")
        return
    else:
        contas.append({
            "agencia":AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print("\n------------------------------------------")
        print("Conta criada com sucesso")
        print("==========================================")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("-" * 42)
        print(linha)
        print("=" * 42)

def main():

    saldo = 0
    limite = 1500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    clear()

    menu = """
    $$$$$ SisBank Diniz $$$$$
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair

    Opção: """

    while True:
        opcao = input(menu)
        if opcao == "1":
            clear()
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            clear()
            saldo, extrato, numero_saques = sacar(
                saldo, 
                limite,
                extrato,  
                numero_saques, 
                LIMITE_SAQUES)
        elif opcao == "3":
            clear()
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            clear()
            novo_usuario(usuarios)
        elif opcao == "5":
            clear()
            numero_conta = len(contas) + 1
            nova_conta(AGENCIA, usuarios, contas, numero_conta)
        elif opcao == "6":
            clear()
            listar_contas(contas)
        elif opcao == "0":
            clear()
            break
        else:
            print("\n------------------------------------------")
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

    
main()
