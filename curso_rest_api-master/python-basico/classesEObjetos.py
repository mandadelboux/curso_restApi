jogador_de_loteria = {
    'nome':'Julia',
    'numeros': (10,23,35,39,57)
}
jogador_de_loteria_2= {
    'nome':'Julia',
    'numeros': (10,23,35,39,57)
}
 
print(jogador_de_loteria == jogador_de_loteria_2)

class JogadorLoteria:
    def __init__(self, nome): #método padrão para instanciar um objeto
        self.nome = nome
        self.numeros = (10,23,35,39,57)

    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria('Toni')
jogador_2 = JogadorLoteria('Shelby') 

print(jogador_1.nome)
print(jogador_2.nome)
print(jogador_1.numeros)

print(jogador_1 == jogador_2)