def insereFrutas(lista):
    fruta = input('Digite o nome da fruta: ')
    lista.append(fruta)

def insereFrutasPilha(lista):
    fruta = input('Digite o nome da fruta: ')
    lista.insert(0,fruta)

def removeFrutas(lista):
    del lista[0]



def imprimeFrutas(lista):
    frase = ''
    tam = len(lista)
    print('\n')
    for i in range(len(lista)):
        if (tam == len(lista)):
            frase+=lista[i]
        elif(tam < len(lista) and tam>1):
                frase += ', '+lista[i]
        else:
            frase += ' e ' + lista[i]
        tam-=1
    print(frase)



frutas = ['maçã', 'banana', 'goiaba', 'pera']
imprimeFrutas(frutas)
insereFrutas(frutas)
imprimeFrutas(frutas)
removeFrutas(frutas)
imprimeFrutas(frutas)