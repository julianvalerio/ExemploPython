#jogo para advinhar numero sorteado
import random
def verificaNum(numsec):
    for num in range(1,7):
        numero=int(input('Tente um numero '))
        if numero < numsec:
            print('O numero sorteado é maior')
        elif numero > numsec:
            print('O numero sorteado é menor')
        else:
            return 'Parabéns, você acertou! \n O numero sorteado foi ' + str(numsec)

    return 'Tentativas encerradas, inicie o jogo novamente.'

numeroSecreto = random.randint(1,20)
print('Tente acertar o número sorteado entre de 1 a 20.')
print('Você tem 5 chances')
print(numeroSecreto)
print(verificaNum(numeroSecreto))

