nota1=int(input('Digite a primeira nota: '))
nota2=int(input('Digite a segunda nota: '))
med = float(nota1+nota2)/2
if(med>=7):
    print('Você esta aprovado com media = {}' .format(med))
elif(med<4):
    print('Você está reprovado com média = {}' .format(med))
else:
    print('Você está de AP3!')
print('Fim do programa')