import math


def getOrdem(lx, ly):
    if len(lx) != len(ly):
        raise Exception("Tamanho diferente")
    
    matriz = []

    listToMatriz = []
    for i in range(len(lx)):
        if i == 0:
            for a in range(len(lx)):
                listToMatriz.append(ly[a])
        else:
            for a in range(len(lx) - i):
                listToMatriz.append(matriz[i-1][a+1] - matriz[i-1][a])
        matriz.append(listToMatriz)
        listToMatriz = []
    
    return matriz


def getP(x, lx, ly):
    if len(lx) != len(ly):
        raise Exception("Tamanho diferente")

    matriz = getOrdem(lx, ly)
    h = lx[1] - lx[0]
    z = (x - lx[0]) / h
    listResult = []

    for i in range(len(lx)):
        if i == 0:
            listResult.append(matriz[i][0])
        elif i == 1:
            listResult.append((z / math.factorial(i)) * matriz[i][0])
        else:
            toAppend = 1
            for j in range(i - 1):
                if j == 0:
                    j+=1
                toAppend *= z - j
            
            toAppend = ((z * toAppend) / math.factorial(i)) * matriz[i][0]
            if i == len(lx) - 1:
                n = len(lx) - 1
                toAppend *= (z - (n - 1))
                toAppend = ((z * toAppend) / math.factorial(i)) * matriz[i][0]
            listResult.append(toAppend)


    return somaVet(listResult)


def funcaoDerivada(x):
    return x + 1

def getEt(x, lx):
    h = lx[1] - lx[0]
    z = (x - lx[0]) / h

    retorno = 1
    n = len(lx) - 1
    for i in range(n):
        if i == 0:
            i+=1
        retorno *= z - i
    
    retorno = (h**(n + 1) * z * retorno) * funcaoDerivada(x) / math.factorial(n + 1)

    return retorno

def somaVet(vet):
    result = 0

    for i in vet:
        result += i

    return result