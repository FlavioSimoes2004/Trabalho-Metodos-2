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
        raise Exception('TAMANHO DIFERENTE')
    
    matriz = getOrdem(lx, ly)
    listResult = []
    h = lx[1] - lx[0]
    z = (x - lx[0]) / h
    
    for i in range(len(lx)):
        if i == 0:
            listResult.append(matriz[i][0])
        else:
            fracao = 1
            for a in range(i):
                fracao *= z - a
                
            fracao = fracao / math.factorial(i)
            listResult.append(fracao * matriz[i][0])
    
    
    return somaVet(listResult)
    


def funcaoDerivada(x):
    return x
    
    
def getEt(x, lx):
    h = lx[1] - lx[0]
    z = (x - lx[0]) / h
    size = len(lx)
    
    result = h**size
    
    for i in range(size):
        result *= z - i
    
    result *= funcaoDerivada(x) / math.factorial(size)
    
    return result
    
    
    
    
def somaVet(vet):
    result = 0
    
    for i in vet:
        result += i
    
    return result
