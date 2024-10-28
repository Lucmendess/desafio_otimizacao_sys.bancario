from Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


    def info(self):
        if len(self.contas) > 0:
            contas = "["
            for c in self.contas:
                contas += f"-{c.__str__()}-,"
            contas = contas[:-1]
            contas += "]"
        else:
            contas = []
        return (f'{self.nome};{self.cpf};{self.data_nascimento};{self.endereco}; contas {contas}')