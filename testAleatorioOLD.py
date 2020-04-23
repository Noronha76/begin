import random

def printL(i):
    for item in i:
        print(item, end=' ')
    print('...')

def somaL(i):
    soma = 0
    for item in i:
        soma += item
    return soma

def mediaL(i):
    soma = somaL(i)
    qtd = len(i)
    return soma / qtd

def pseudoA(i):
    count = 0
    anterior = 0
    lista = []
    dif = 0
    ldif = []
    while count < i:
        if random.randrange(1,10) == 5:
            lista.append(1)
            atual = count
            dif = atual - anterior
            ldif.append(dif)
            anterior = atual
        else:
            lista.append(0)        
        count += 1
    return ldif

def newA(i):
    count = 0
    anterior = 0
    lista = []
    dif = 0
    ldif = []
    while count < i:
        if felipeA(1,10) == 5:
            lista.append(1)
            atual = count
            dif = atual - anterior
            ldif.append(dif)
            anterior = atual
        else:
            lista.append(0)        
        count += 1
    return ldif

def felipeA(i,ii):
    return (random.randrange(i,ii) + random.randrange(i,ii) + random.randrange(i,ii)) / 3

aleatorio1 = pseudoA(1000)
aleatorio2 = newA(1000)
    
print('pseudos aleatórios : ')
printL(aleatorio1)
print('Ocorrências : {0}  Soma : {1}    Média : {2:.2f}'.format(len(aleatorio1) , somaL(aleatorio1) , mediaL(aleatorio1)))
print('pseudos aleatórios, método novo : ')
printL(aleatorio2)
print('Ocorrências : {0}  Soma : {1}    Média : {2:.2f}'.format(len(aleatorio2) , somaL(aleatorio2) , mediaL(aleatorio2)))

