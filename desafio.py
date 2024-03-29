menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

class Operacao():
    def __init__(self) -> None:
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3 

    def depositar(self, st_valor):    
        valor = float(st_valor)
        if valor >0 :
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada")
        else:
            print("Operação falhou! o valor informado é inválido")

    def sacar(self, st_valor):
        valor = float(st_valor)
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! Valor do sque excede o limite de {self.limite:.2f}")
        elif excedeu_saques:
            print(f"Máximo de {self.LIMITE_SAQUES} saques excedido")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Operação realizada")
        else:
            print("Operação falhou! O valor informado não é válido")  
        
    def imprimir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

op = Operacao()
while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        st_valor = input('Informe o valor do depósito:\n')
        op.depositar(st_valor)
    
    elif opcao == "s":
        st_valor = input('Informe o valor do saque:\n')
        op.sacar(st_valor)
    
    elif opcao == "e":
        op.imprimir_extrato()
    
    elif opcao == "q":
        break
    
    else:
        print(f"A opção {opcao}, não corresponde a uma operação válida, tente novamente.")
        
    
        






