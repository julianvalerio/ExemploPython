def fatorial(n):
    resultadofat = 1
    contador = 1
    while contador < n:
        contador += 1
        resultadofat *= contador
    return resultadofat

numero = int(input('Digite um numero: '))
print(fatorial(numero))