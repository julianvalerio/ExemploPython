'''
#tipo que pode possuir valore diferentes
lista = ['gato', 'cachorro', 'macaco', 1, 2, 3]

print(lista)
print(lista[0]+lista[3])
lista2 = ['pai', 'mae', 'filho']
#concatenar listas
lista3 = lista+lista2
print(lista3)


listaMedia = []
while True:
    print('Entre com a nota do aluno '+ str(len(listaMedia)+1)+
          ' ou pressione enter para sair.')
    media = input()
    if media == '':
        break
    listaMedia = listaMedia + [media]
print('As medias são: ')
for media in listaMedia:
    print(' '+ media)

'''
def verificaNome():
    print('Pesquise um nome na lista: ')
    name = input()
    if name not in Listanomes:
        print('Nome não encontrado')
    else:
        print('Nome encontrado.')

Listanomes = []
while True:
    print('Entre com o nome do aluno '+ str(len(Listanomes)+1)+ ' ou pressione enter para sair.')
    nomes = input()
    if nomes == '':
        break
    Listanomes = Listanomes + [nomes]
print('As nomes são: ')
for nomes in Listanomes:
    print(' '+ nomes)
verificaNome()

