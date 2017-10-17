from random import randint

num1 = int(input('Digite o limite inferior: '))
num2 = int(input('Digite o limite superior: '))
cont = 0
while(num1<(num2-1)):
    if(((num1+1)%2)==0):
        cont+=1
    num1+=1
print('A quantidade de números pares no intervalo é: ', cont)





quant = int(input("Digite a quantidade de numeros aleatorios que deseja somar: "))
i=0
soma=0
while(i<quant):
    soma+=randint(1,10)
    i+=1
print('A soma dos numeros aleatórios é igual a: ', soma)
