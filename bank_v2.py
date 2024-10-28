from time import sleep
from datetime import datetime
from PessoaFisica import PessoaFisica
from Cliente import Cliente
from Conta import Conta
from Historico import Historico
from Saque import Saque
from Transacao import Transacao

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

def cadastrar_cliente(arq, pessoafisica: PessoaFisica):
    if isinstance(pessoafisica, PessoaFisica):
        try:
            with open(arq, 'at', encoding="utf-8") as a:
                a.write(pessoafisica.info() + '\n')
                print(f'Novo cadastro {pessoafisica.nome} feito com sucesso!')
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

def buscarcliente(caminho_do_arquivo, cpf_cliente):
    lista_cliente = []
    try:
        with open(caminho_do_arquivo, 'rt', encoding='utf-8') as a:
            lista_cliente = a.readlines()
        for line in lista_cliente:
            if line.__contains__(cpf_cliente):
                line = line.replace('\n', '')
                campos = line.split(';')
                nome = campos[0]
                data_nascimento = campos[2]
                endereco = campos[3] 
                #TODO extrair contas para uma lista
                contas = campos[4]
                return PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_cliente, endereco=endereco)
            
    except Exception as ex:
        print(f'Ocorreu ERRO no cadastro de dados {ex.args}')
    


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    arq_cliente = 'Clientes.txt'
    arq_conta = 'Contas.txt'
    
    if not arquivoExiste(arq_cliente):
        criarArquivo(arq_cliente)
    if not arquivoExiste(arq_conta):
        criarArquivo(arq_conta)

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saque = 3

    while True:
        resposta = menu(['Depositar', 'Sacar', 'Extrato', 'Novo Cliente', 'Nova Conta', 'Listar Clientes', 'Listar Contas', 'Sair'])
        
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
            cabecalho('Novo Cliente')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
            endereco = input('Endereço: ')
            boby = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
            cadastrar_cliente(arq_cliente, boby)

        elif resposta == 5:
            cabecalho('Nova Conta')
            nome = input('Nome do Titular: ')
            saldo = float(input('Saldo: '))
            limite = float(input('Limite: '))
            cadastrar_conta(arq_cliente)

        elif resposta == 6:
            lerArquivo(arq_cliente)

        elif resposta == 7:
            lerArquivo(arq_conta)

        elif resposta == 8:
            print('Saindo do sistema... Até logo!')
            break

        sleep(2)



if __name__ == "__main__":
    main()