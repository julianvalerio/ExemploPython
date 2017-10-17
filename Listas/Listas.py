import copy
#lista de listas ou matrizes
notas = [['nota1', 'nota2', 'nota3'], [7, 8.2, 6]]
print(notas[0][1],notas[1][1])



#uso do for#

nomes = ['julian', 'rodrigues', 'valerio']
#for i in ['julian', 'rodrigues', 'valerio']

for i in range(len(nomes)):
    print('Indice '+str(i)+ ' descrição ' + nomes[i])

#dessa forma conseguimos percorrer toda lista
#o tamanho da lista é descoberto através da função len
#encontrar valor em uma lista utilizando métodos, metodos utilizam valores quando são chamados

print(nomes.index('rodrigues'))

nomes.append('marta')

#nomes.insert(2,'pedro')
print(nomes)

#insert insere o elemento em qualquer posição da lista, necessário indice
nomes.insert(2,'pedro')
print(nomes)

#removendo com del ou remove
del nomes[-1]
nomes.remove('pedro')
print(nomes)




#exercício: crie uma lista frutas em seguida crie uma função que receba a lista e imprima
#todos seus valores separados por vírgula e que o último valor será separado por e
#ordenando os valores da lista sort
#não funciona com listas heterogêneas


nomes.insert(0,'Pedro')
nomes.sort(reverse=True)
print(nomes)





#padrão de ordenação ASCII
nomes.append('Julian')
nomes.sort(key=str.lower)
print(nomes)




#tipo tuple, semelhante a lista mas não pode ser modificado
tupla=('julian',)
print(tupla[0])




#atribuição por referência
disc = 'matematica'
cad = disc
print(cad)
disciplinas = ['programação', 'Banco de dados', 'ED', 'ihc']
cadeiras = disciplinas
cadeiras[0]='4º semestre'
print(disciplinas)
cadeiras.insert(1,'programação')
print(cadeiras)




#python utiliza referências sempre que os valores são mutáveis
#função copy
#permite copiar ou duplicar uma lista

materias = copy.copy(disciplinas)
print(materias)
materias.append('python')
print(materias)
print(disciplinas)