class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_feitos = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_feitos < 3:
            if valor > 0 and valor <= 500:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques.append(valor)
                    self.saques_feitos += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("Valor do saque inválido. O valor máximo por saque é R$ 500.00.")
        else:
            print("Limite diário de saques atingido. Você não pode fazer mais saques hoje.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

def menu():
    conta = ContaBancaria()

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
        elif escolha == '2':
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif escolha == '3':
            conta.extrato()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

menu()
