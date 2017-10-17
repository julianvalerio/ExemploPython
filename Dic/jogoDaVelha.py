#criando jogo da velha
#precisamos criar um dicionário que represente um tabuleiro
#a estrutura a seguir representa nosso tabuleiro
tabuleiro = {'top-e':' ', 'top-m': ' ', 'top-d': ' ',
             'mid-e':' ', 'mid-m': ' ', 'mid-d': ' ',
             'bot-e':' ', 'bot-m': ' ', 'bot-d': ' '}
#vamos criar uma função para imprimir o tabuleiro
def printTabuleiro(tabuleiro):
    print(tabuleiro['top-e']+'|'+tabuleiro['top-m']+'|'+tabuleiro['top-d'])
    print('-+-+-')
    print(tabuleiro['mid-e'] + '|' + tabuleiro['mid-m'] + '|' + tabuleiro['mid-d'])
    print('-+-+-')
    print(tabuleiro['bot-e'] + '|' + tabuleiro['bot-m'] + '|' + tabuleiro['bot-d'])

#testando a função imprime
printTabuleiro(tabuleiro)

#jogadas
jogada = 'X'
for i in range(9):
    printTabuleiro(tabuleiro)
    print('Jogada para '+jogada+ '. Marcar espaço: ')
    marcar = input()
    tabuleiro[marcar]=jogada
    if jogada=='X':
        jogada='0'
    else:
        jogada='X'
printTabuleiro()