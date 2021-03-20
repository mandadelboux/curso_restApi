class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

fabio = Funcionario('Fábio', 7000)
print(fabio.dados())

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()

lucas = Admin('Lucas', 14000)
lucas.atualizar_dados('Luquinhas')
print(lucas.dados())

