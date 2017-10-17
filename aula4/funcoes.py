def Name():
    print('Julian')
    print('Rodrigues')
    print('Valerio')

def name(nome):
    print('Seu nome é ' + nome)

name('Julian')

nome2 = 'Valerio'
name(nome2)

Name()

def fullName():
    return 'Julian Rodrigues Valerio'

nomeCompleto=fullName()
print(nomeCompleto)
print(fullName())