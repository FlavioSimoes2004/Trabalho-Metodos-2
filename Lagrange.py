import math

def getP(x, listx, ly):
    if len(listx) != len(ly):
        raise Exception("Tamanho diferente")

    listToResult = []
    Li = None
    for i in range(len(ly)):
        Li = getLI(x, i, listx)
        listToResult.append(ly[i] * Li)

    return somaVet(listToResult)


def getLI(x, pos, listx):
    listCima = []
    listBaixo = []

    for i in range(len(listx)):
        if pos != i:
            listCima.append(x - listx[i])
            listBaixo.append(listx[pos] - listx[i])


    return multiVet(listCima) / multiVet(listBaixo)
    



def multiVet(vet):
    if len(vet) == 0:
        return 0
    
    result = 1
    for i in vet:
        result *= i
    return result

def somaVet(vet):
    result = 0

    for i in vet:
        result += i

    return result




def funcaoDerivada(x):
    return (24 * x) - 18

def getErroTrunc(x, listx):
    #nao esquecer de mudar a funcao derivada
    fx = funcaoDerivada(x)
    if fx == 0:
        return 0
    
    divisao = funcaoDerivada(x) / (math.factorial(len(listx)))
    listToResult = []

    for i in listx:
        listToResult.append(x - i)

    return multiVet(listToResult) * divisao