minha_variavel = 'ola'
print(len(minha_variavel))
print(minha_variavel[0])


# range(star, stop, step) - Obrigatório o stop
print(range(10))
print(list(range(10)))

# lista de números impares
print(list(range(1,12,2)))

# lista de números pares
numeros_pares = list(range(0,12,2))
for numero in numeros_pares:
    print(numero ** 2)

# while
x = 0
while x <= 10:
    print(x**3)
    x += 2 #Incrimentar
print('\n*****************\n')
usuario_quiser = True
while usuario_quiser == True:
    usuario_input = input('Quer continuar? ')
    if ((usuario_input == 'N' ) or (usuario_input == 'Não')):
        usuario_quiser = False
        print('Então tchau, bocó!')
    else:
        print('Então vai, man')