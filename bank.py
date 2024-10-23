from time import sleep
from datetime import datetime

def linha(tam=23):
    return '-*=*-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())

def menu(lista):
    cabecalho('Menu de Sistema Bancário')
    for i, item in enumerate(lista, 1):
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
    print(linha())
    return leiaInt('Digite uma opção válida: ')

def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite uma opção válida!\033[m')
        except KeyboardInterrupt:
            print('\033[31mERROR: Processo interrompido pelo usuário!\033[m')
            return 0

def arquivoExiste(nome):
    try:
        open(nome, 'rt').close()
        return True
    except FileNotFoundError:
        return False

def criarArquivo(caminho_arquivo):
    try:
        open(caminho_arquivo, 'wt+').close()
        print(f'Arquivo {caminho_arquivo} criado com sucesso!')
    except:
        print(f'Houve um ERRO na criação do arquivo {caminho_arquivo}')

def lerArquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rt') as a:
            cabecalho(f'Listar {caminho_arquivo}')
            for linha in a:
                print(linha.strip())
    except Exception as e:
        print(f'ERRO ao mostrar o {caminho_arquivo}: {e}')

def cadastrar_usuario(arq, nome, cpf, data_nascimento, endereco):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome};{cpf};{data_nascimento};{endereco}\n')
            print(f'Novo cadastro {nome} feito com sucesso!')
    except:
        print('Ocorreu ERRO no cadastro de dados')

def cadastrar_conta(arq_conta, nome, agencia, saldo, limite):
    try:
        with open(arq_conta, 'at') as a:
            a.write(f'{nome};{agencia};{saldo};{limite}\n')
            print(f'Conta criada para {nome} com sucesso!')
    except:
        print('Ocorreu ERRO no cadastro de dados')

def deposito(saldo, valor):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo

def sacar(saldo, valor, numero_saques, limite_saque):
    if valor > saldo:
        print("Saldo insuficiente!")
    elif numero_saques >= limite_saque:
        print("Número máximo de saques excedido.")
    else:
        saldo -= valor
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    arq_usuario = 'Usuarios.txt'
    arq_conta = 'Contas.txt'
    
    if not arquivoExiste(arq_usuario):
        criarArquivo(arq_usuario)
    if not arquivoExiste(arq_conta):
        criarArquivo(arq_conta)

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saque = 3

    while True:
        resposta = menu(['Depositar', 'Sacar', 'Extrato', 'Novo Usuário', 'Nova Conta', 'Listar Usuários', 'Listar Contas', 'Sair'])
        
        if resposta == 1:
            valor = float(input("Digite o valor do depósito: "))
            saldo = deposito(saldo, valor)
            extrato += f"Depósito: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"

        elif resposta == 2:
            valor = float(input("Digite o valor do saque: "))
            saldo, numero_saques = sacar(saldo, valor, numero_saques, limite_saque)
            if valor <= saldo + valor:
                extrato += f"Saque: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"

        elif resposta == 3:
            exibir_extrato(saldo, extrato)

        elif resposta == 4:
            cabecalho('Novo Usuário')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
            endereco = input('Endereço: ')
            cadastrar_usuario(arq_usuario, nome, cpf, data_nascimento, endereco)

        elif resposta == 5:
            cabecalho('Nova Conta')
            nome = input('Nome do Titular: ')
            agencia = input('Agência: ')
            saldo = float(input('Saldo: '))
            limite = float(input('Limite: '))
            cadastrar_conta(arq_conta, nome, agencia, saldo, limite)

        elif resposta == 6:
            lerArquivo(arq_usuario)

        elif resposta == 7:
            lerArquivo(arq_conta)

        elif resposta == 8:
            print('Saindo do sistema... Até logo!')
            break

        sleep(2)

if __name__ == "__main__":
    main()