def atm(saldo, idade, nome_completo):
    x = int(input('''
        Digite (1) para saque \n
        Digite (2) para depósito \n
        Digite (3) para empréstimo \n
        Digite (4) para visualizar informações \n
        Digite (Qualquer outro caracter) para sair--->
    '''))
    try:
        if x == 1:
            saque(saldo)
        elif x == 2:
            deposito(saldo)
        elif x == 3:
            emprestimo(saldo, idade)
        elif x == 4:
            visualizar_info(nome_completo, saldo, idade)
        else:
            print('Operação finalizada')
    except:
        print('Operação finalizada')


def visualizar_info(nome_completo, saldo, idade):
    print(f'\n {nome_completo} - {idade} anos \n Saldo: R$ {saldo}')
    return atm(saldo, idade, nome_completo)


def saque(saldo):
    valor = float(input('Digite o valor do saque: '))
    if valor < 1000 and saldo >= valor:
        saldo = saldo - valor
        print(f'SALDO: {saldo}')
    else:
        print('Não foi possivel realizar o saque')
    return atm(saldo, idade, nome_completo)


def deposito(saldo):
    valor = float(input('Digite o valor do depósito: '))
    if valor < 5000:
        saldo = saldo + valor
        print(f'SALDO: {saldo}')
    else:
        print('O valor limite para depósito é de R$ 5000.00 reais')
    return atm(saldo, idade, nome_completo)


def emprestimo(saldo, idade):
    if idade > 21:
        valor_emprestimo = float(input('Digite o valor de emprestimo: '))
        if (saldo >= 1000) and (valor_emprestimo >= 2000 and valor_emprestimo <= saldo*15):
            print('EMPRESTIMO ACEITO :)')
            saldo = saldo + valor_emprestimo
            print(f'SALDO: {saldo}')
        else:
            print('Empréstimo recusado devido ao saldo')
    else:
        print('Idade mínima para empréstimo é de 21 anos')
    return atm(saldo, idade, nome_completo)


print('Bem-vindo(a) ao GROGER BANK, para continuar cadastre as seguintes informações: ')
nome_completo = input('Digite o seu nome completo: ')
idade = int(input('Digite sua idade: '))
saldo = float(input('(Simulação de Saldo) - Digite a simulação de saldo: '))
atm(saldo, idade, nome_completo)