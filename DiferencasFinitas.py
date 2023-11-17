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
    #incompleto
    if len(lx) != len(ly):
        raise Exception("Tamanho diferente")

    matriz = getOrdem(lx, ly)
    h = lx[1] - lx[0]
    z = (x - lx[0]) / h
    listResult = []

    for i in range(len(lx)):
        if i == 0:
            listResult.append(matriz[i][0])
            continue
        else:
            toAppend = (z / math.factorial(i)) * matriz[i][0]
            listResult.append(toAppend)


    return somaVet(listResult)


def somaVet(vet):
    result = 0

    for i in vet:
        result += i

    return result