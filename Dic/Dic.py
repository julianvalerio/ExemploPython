#dicionarios
#oferecem maneira flexível de organizar e acessar dados
#é uma coleção de diversos valores
#os valores no dicionário não sao ordenados
#os indices (chaves) podem possuir valores diferentes de inteiro
#par chave valor

caracteristica = {'data_nasc': '18/03/89', 'sexo': 'masculino', 'altura': '1.77'}
#os valores podem ser acessador por meio das chaves

print('Sua altura é '+ caracteristica['altura'])

#acessar chave inexistente causa erro
#print('Sua cor é '+ caracteristica['cor'])

#comparação entre listas e dicionários
animais1=['cachorro', 'gato', 'macaco']
animais2=['gato', 'cachorro', 'macaco']
print(animais1==animais2)

caracteristica2 = {'sexo': 'masculino', 'data_nasc': '18/03/89', 'altura': '1.77'}
print(caracteristica==caracteristica2)

#verificar valores em um dicionario
#keys values items
for v in caracteristica2.values():
    print(v)

for i in caracteristica2.keys():
    print(i)

for j in caracteristica2.items():
    print(j)

for l, m in caracteristica2.items():
    print('chave: ' + l + ' valor: ' + m)

# verificar se determinado valor ou chave está presente
print('nacionalidade' in caracteristica2.keys())

#metodo get
compras = {'arroz': '3kg', 'bananas': 'uma dúzia', 'óleo': '1 L'}
print('Eu comprei '+compras.get('arroz', 0) + ' de arroz')
print('Eu comprei '+str(compras.get('ovos', 0)) + ' ovos')



#setdefault
#permite definir um valor padrão para uma chave ainda sem valor
caracteristica2.setdefault('cor', 'indefinida')
for l, m in caracteristica2.items():
    print('chave: ' + l + ' valor: ' + m)

#tentar mudar valor de setdefault
caracteristica2.setdefault('cor', 'pardo')

#