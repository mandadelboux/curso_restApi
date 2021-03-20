# args ==> argumentos
# kwargs ==> keyword arguments (argumentos de palavra-chave)

def meu_metodo(arg1, arg2):
    return arg1 + arg2


def meu_metodo_longo(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5


print(meu_metodo(2,2))
print(meu_metodo_longo(2,2,2,2,2))


def minha_lista_somada(lista):
    return sum(lista)

print(minha_lista_somada([2,2,2,2,2]))


def soma_simplificada(*args): #praticamente uma lista
    return sum(args)

print(soma_simplificada(1,2,3,4,5,6))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

# args antes do kwargs
metodo_kwargs(3,'saa', 4, 'qualquer', nome='Amanda', idade = 20)
print(metodo_kwargs())
