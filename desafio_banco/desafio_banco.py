menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print ("Operação falhou! O valor informado não é válido.")
        


    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente para sacar.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque é maior que seu saldo.")
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saque.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Operação falhou! Você não tem saldo suficiente para sacar.")

    elif opcao == "e":
        print ("\n============Extrato============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("================================")

    elif opcao == "q":
        print("Obrigado por usar nossos serviços. Volte sempre!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma nova opção.")
