# [o que vc quer fazer]
print([x+10 for x in range(5)])

print(list(range(0,10,2)))

# Pegando números pares
print([n for n in range(11) if n % 2 == 0])
# Numeros impares
print([n for n in range(11) if n % 2 == 0])

# Teste buscando nomes
listaDeNomes = ['Amanda', 'Juliana', 'Nicolas']

pergunta = input('Adicionar pessoa ou procurar? ')
# pergunta.lower()

if (pergunta == 'adicionar'):
    add_nome = input('Insira o nome: ')
    listaDeNomes.append(add_nome)
    print('Nome: {} adicionado com sucesso!'.format(add_nome))
elif (pergunta == 'procurar'):
    quem_nome = input('Quem você quer achar? ')
    


