#crie um programa para salvar as datas de aniversários, apenas mes e dia

aniversarios={'julian': '18 de março', 'andressa': '02 de maio', 'arthur': '09 de julho'}
while True:
    print('Digite um nome: (pressione apenas enter para sair)')
    nome=input()
    if nome=='':
        break
    if nome in aniversarios:
        print(aniversarios[nome] + ' é o aniversário de ' + nome)
    else:
        print('A data do aniversário de '+ nome + ' não está cadastrada')
        print('Qual o seu aniversário: ')
        bday = input()
        aniversarios[nome]=bday
        print('A lista de aniversário foi atualizada!')