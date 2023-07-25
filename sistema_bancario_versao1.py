#Versão 1 do sistema bancário simples.
#Apenas 1 usuário
#Depósito:não pode ser possível depositar valores negativos
#Saque:Limite por saque de 500 reais. Apenas 3 saques por dia.
#Extrato:Deve conter todas as operações de saque e depósito no formato R$xxx.xx

menu = """
Informe a operação desejada

[1] Depositar
[2] Sacar
[3] Extrato
[4] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print ("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "2":
        print ("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print ("\n======= Extrato =======")
        print(" Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print ("=======================")

    elif opcao == "4":
        break

    else:
        print ("Operação inválida. Por favor, seleciona novamente a operação desejada.")
