print('ola mundo!')
nome = input('Qual é o seu nome: ')
print('Bem vindo ', nome)
print('Digite um numero: ')
num = int(input())
if (num>10):
    print('O numero digitado é maior que 10')
elif (num<0):   
    print('O numero digitado é menor que zero')
else:
    print('O numero digitado está entre 0 e 10')