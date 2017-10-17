

'''
def spam():
    codigo=301214
    print(codigo)

spam()
#print(codigo)

#sample1
def spam():
    ovos = 99
    bacon()
    print(ovos)

def bacon():
    presunto=101
    ovos=0
    print(ovos)
spam()

#sample2 lendo variavel global localmente
def spam():
    print(ovos)
ovos=42
spam()
print(ovos) 

smaple3 variaveis com o mesmo nome, quantas variáveis temos

def spam():
    ovos='spam local'
    print(ovos)
def bacon():
    ovos='bacon local'
    print(ovos)
    spam()
    print(ovos)
ovos = 'global'
bacon()
print(ovos)

sample4 instrução global
def spam():
    global ovos
    ovos = 'spam'
def bacon():
    ovos = 'bacon'
def presunto():
    print(ovos)
ovos = 42
spam()
print(ovos)

smaple 5 erro variável utilizada antes de atribuir'''
def spam():
    ovos='bacon'
    print(ovos)
ovos = 'global'
spam()
