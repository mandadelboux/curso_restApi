import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print("**** Embrulhando função no decorador *******")
        funcao()
        print("****** Fechando Embrulho *******")
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print("Eu sou uma função!")

minha_funcao()