notas = [3,4,5,6,4,8]
print(len(notas))
print('O que tem dentro de notas: {}'.format(notas))
notas.append(10)
print('Atualizando...')
print(len(notas))
print('O que tem dentro de notas: {}'.format(notas))


media = sum(notas)/len(notas)
print('Média das notas {}'.format(media))
