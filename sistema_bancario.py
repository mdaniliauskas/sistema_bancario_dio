# Desafio 1 - Python - Sistema bancário

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ()
numero_saques = 0
LIMITE_SAQUES = 3
txt_valor = """
Informe o valor desejado: 
"""
deposito = 0
extrato = ""

while True:
    opcao = int((input(menu)))
    
    if opcao == 1:
        deposito = float(input(txt_valor))
        if deposito > 0:            
            saldo += deposito                                   
            extrato += f"Depósito: R$ {deposito:.2f}\n"                          
        else:
            print("\nValor informado não é válido\n")

    elif opcao == 2: 
        saque = float(input(txt_valor))         
        if numero_saques > LIMITE_SAQUES:                               
            print("\nOperação não realizada, número de saques diários excedidos\n")
        
        elif saque > saldo:
            print("\nOperação inválida, valor de saque acima do disponível em saldo\n")     
        
        elif saque > 500:
            print("\nLimite máximo de saque: R$ 500\n")        
        
        elif saldo > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque...: R$ {saque:.2f}\n"

    elif opcao == 3:
        if extrato != 0: 
            print("\n *********** Extrato ***********\n")
            print(extrato)
            print(f"\nSaldo...: R$ {saldo:.2f}\n")
            print("*******************************\n")
        else:
            print("Sem movimentações no período")

    elif opcao == 0:
        print("Obrigado por utilizar nossos serviços\n")
        break

    else:
        print("""
              
              Operação inválida, por favor, escolha uma operação do menu, sendo 0 para sair"
              
              """)

