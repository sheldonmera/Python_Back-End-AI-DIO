menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
deposito = 0
limite = 500
extrato = ""
numero_saques = 0
valor_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        deposito = int(input('Insira o valor do deposito R$ '))
        
        if deposito > 0 :
            saldo += deposito
            extrato += f" Deposito de R${deposito:.2f} recebido ! \n"
            
    elif opcao == "s":
        if  numero_saques < LIMITE_SAQUES:
            valor_saque = int(input("Insira o valor do Saque R$"))
            
            if valor_saque > saldo:
                print("Saldo Insuficiente Para Saque".center(40, "!"))
            
            elif valor_saque <= 0:
                print("Valor Incorreto Para Saque".center(40, "!"))
                
            else:
                saldo = saldo - valor_saque
                numero_saques += 1
                extrato += f"\n Saque de R${valor_saque} \n"
                 
        else:
                print(" Saque Excede o Limite".center(28, "!"))
            
    elif opcao == "e":
        extrato += f" Saldo atual R${saldo:.2f} \n"
        print(extrato)
        
    elif opcao == "q":
        break