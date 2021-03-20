import datetime


class Funcionario():
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

# usando a classe para determinar a mudança em todos os objetos
    @classmethod
    def definir_novo_aumento(cls, novo_aumento): #cls - própria classe
        cls.aumento = novo_aumento

    @staticmethod
    def dia_util(dia):
        # segunda = 0 e domingo = 6
        if (dia.weekday() == 5 or dia.weekday() == 6 ):
            return False 
        return True

fabio = Funcionario('Fábio', 7000)
fabio.aplicar_aumento()
print(fabio.dados())

Funcionario.definir_novo_aumento(1.05)

leticia = Funcionario('Leticia', 8000)
leticia.aplicar_aumento()
print(leticia.dados())

corVencedor = datetime.date(2020,12,13) #Domingão
print(Funcionario.dia_util(corVencedor))

minha_data = datetime.date(2021,1,12) #Domingão
print(Funcionario.dia_util(minha_data))
