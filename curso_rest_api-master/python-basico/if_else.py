listaPessoas = ['Amanda','Fernanda']
pessoa = input('Nome de pessoa que vc conhece: ')

if (pessoa in listaPessoas):
    print("Você conhece essa pessoa!\n")
else:
    pergunta = input('\nVocê não conhece essa pessoa :(\nDeseja adicionar em sua lista? ')
    if(pergunta == 'Sim'):
        listaPessoas.append(pessoa)
        print('\nNova pessoa adicionada na lista!\n')
    elif (pergunta == 'Não'):
        print('\nOkay! :)')
    else:
        print('Resposta inválida!')

def mostrarLista:
    print(listaPessoas)