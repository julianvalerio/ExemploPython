import pprint
mensagem = 'Teste de contagem de caracteres.'
cont = {}
for caractere in mensagem:
    cont.setdefault(caractere,0)
    cont[caractere]=cont[caractere]+1

print(cont)