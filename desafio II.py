
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
   
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):    
    if valor>0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\nOperação não realizada, o valor informado é inválido")
    
    return saldo, extrato

def emitir_extrato(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def menu():
    menu = """\n
    ============== MENU ==============
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\t\tSair
    =>"""

    return input(menu)

def filtrar_usuario(cpf_usuario, lista_usuarios):
    lista_usuarios_filtrada = [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf_usuario]
    return lista_usuarios_filtrada[0] if lista_usuarios_filtrada else None

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números):\n')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('CPF já é um usuário cadastrado!')
        return
    
    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"cpf":cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!!!")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário:\n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('Conta não poderá ser criada, usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        Conta:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(saldo = saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES
                                )

        elif opcao == "e":
            emitir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()




