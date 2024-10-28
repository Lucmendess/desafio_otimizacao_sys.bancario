from PessoaFisica import PessoaFisica
from bank import cadastrar_cliente
from bank import buscarcliente
from Conta import Conta

boby = PessoaFisica(nome="AnaBolada", data_nascimento="01/01/1800", cpf="158811424", endereco="Rua da ladeira quebrada, fim do mundo, Brasília")
topeira_eu = PessoaFisica(nome="Fulano de tal", data_nascimento="01/01/1800", cpf="000000000", endereco="Rua da ladeira quebrada, fim do mundo, Brasília")
print(f"{str(type(boby)).split(" ")[1].split(".")[1][:-2]}")
conta_cliente = Conta(boby)
boby.adicionar_conta(conta=conta_cliente)
print(isinstance(boby, PessoaFisica))
conta_cliente = Conta(boby)
conta_cliente.depositar(9000)
boby.adicionar_conta(conta=conta_cliente)

cadastrar_cliente(arq="teste.txt", pessoafisica=boby)
      
cadastrar_cliente(arq="teste.txt", pessoafisica=topeira_eu)

buscarcliente(caminho_do_arquivo="teste.txt", cpf_cliente="000000000")
      

