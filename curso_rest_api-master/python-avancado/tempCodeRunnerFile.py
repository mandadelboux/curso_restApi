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
    print(listaDeNomes.find(quem_nome))
    