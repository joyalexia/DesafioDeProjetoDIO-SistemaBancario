menu = '''
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

'''



saldo = 0
limite = 500
extrato = ''
numeroDeSaques = 0
LIMITES_SAQUES = 3

while True:
    print(menu)
    opcao = int(input('Digite aqui: '))

    if opcao == 1:
        print('----------Desposito---------')
        valor = float(input('Digite o valor que deseja depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}'
            print('Depósito efetuado com sucesso!')
        
        else:
            print('Valor inválido.')

    
    elif opcao == 2:
        print('---------Saque--------')
        valor = float(input('Digite o valor que deseja sacar: '))

        execedeulimite = valor > limite
        execedeuSaldo = valor > saldo
        execedeuSaques = numeroDeSaques >= LIMITES_SAQUES

        if execedeulimite:
            print(f'Não foi possível concluir a operação. Limite para saque é de R${limite:.2f}')
        
        elif execedeuSaldo:
            print('Não foi possível concluir a operação. Valor não compaivel com seu saldo')
        
        elif execedeuSaques:
            print('Não foi possível concluir a operação. Número de saques foi excedido.')

        elif valor > 0:
            saldo -=valor
            extrato += f'\nSaque: R${valor:.2f}'
            numeroDeSaques += 1
            print('Saque efetuado com sucesso!')
        
        else:
            print('Valor inválido.')
    
    elif opcao == 3:
        print('_____________Extrato______________')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("__________________________________")

    elif opcao == 4:
        print('Volte Sempre!')
        break

    else:
        print('ERRO: Inválido, selecione novamente a operação desejada')