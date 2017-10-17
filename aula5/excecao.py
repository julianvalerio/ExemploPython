'''def excecao(dividePor):
    return 42/dividePor
print(excecao(10))
print(excecao(2))
print(excecao(0))
print(excecao(1))

def trataExcecao(dividePor):
    return 42/dividePor
try:
    print(trataExcecao(10))
    print(trataExcecao(2))
    print(trataExcecao(0))
    print(trataExcecao(1))
except ZeroDivisionError:
    print('Argumento inválido!')
'''
#corrigindo a excecao

def trataExcecao(dividePor):
    try:
        return 42/dividePor
    except ZeroDivisionError:
        print('Divisão inválida!')

print(trataExcecao(10))
print(trataExcecao(2))
print(trataExcecao(0))
print(trataExcecao(1))