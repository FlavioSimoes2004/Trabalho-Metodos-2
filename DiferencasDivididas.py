import math

def funcao(x):
    return x ** 2


def getOrdem(list):
    newMatrix = []
    n = list.__len__()

    for i in range(n):
        print(i)
        newMatrix.append(diferencas(list, i))
        
    return newMatrix



def diferencas(list, ordem):
    n = list.__len__()
    listReturn = []
    listParameter = []

    got = 0
    pos = 0
    while(pos < n):
        listParameter.append(list[pos])
        got+=1
        if got == ordem + 1:
            got = 0
            listReturn.append(calcInter(listParameter, ordem))
            listParameter = []
            pos-=ordem
        pos+=1
    
    return listReturn

def calcInter(list, ordem):
    list1 = [] #x0
    list2 = [] #x1

    if ordem == 0:
        return funcao(list[0])
    
    got = 0
    for i in range(list.__len__() - 1):
        list1.append(list[i])
        list2.append(list[i + 1])
        got += 1
        if got == ordem:
            break

    divisao = list[ordem] - list[0]
    ordem -= 1
    return (calcInter(list2, ordem) - calcInter(list1, ordem)) / divisao



def getOrdem2(listx, ly):
    global listy
    listy = list.copy(ly)

    newMatrix = []
    n = listx.__len__()

    for i in range(n):
        #print(i)
        newMatrix.append(diferencas2(listx, i))
        
    return newMatrix

def diferencas2(list, ordem):
    n = list.__len__()
    listReturn = []
    listParameter = []

    got = 0
    pos = 0
    while(pos < n):
        listParameter.append(list[pos])
        got+=1
        if got == ordem + 1:
            got = 0
            listReturn.append(calcInter2(list, listParameter, ordem))
            listParameter = []
            pos-=ordem
        pos+=1
    
    return listReturn

def calcInter2(listx, list, ordem):
    list1 = [] #x0
    list2 = [] #x1

    if ordem == 0:
        for i in range(listx.__len__()):
            if list[0] == listx[i]:
                return listy[i]
    
    got = 0
    for i in range(list.__len__() - 1):
        list1.append(list[i])
        list2.append(list[i + 1])
        got += 1
        if got == ordem:
            break
    
    divisao = list[ordem] - list[0]
    ordem-=1
    return (calcInter2(listx, list2, ordem) - calcInter2(listx, list1, ordem)) / divisao


def getP(x, listx, ly):
    matriz = getOrdem2(listx, ly)
    listResult = []
    listToResult = []
    for i in range(len(listx)):
        if i == 0:
            listResult.append(matriz[0][0])
        else:
            for j in range(i + 1):
                if j == i:
                    listToResult.append(matriz[i][0])
                else:
                    listToResult.append(x - listx[j])
            listResult.append(multiVetor(listToResult))
            listToResult = []
    
    return somaVetor(listResult)


def multiVetor(vet):
    if len(vet) == 0:
        return 0
    
    result = 1
    for i in vet:
        result *= i
    return result


def somaVetor(vet):
    result = 0

    for i in vet:
        result += i
    return result


def funcaoDerivada(x):
    return 0

def getErroTrunc(x, listx):
    #nao esquecer de mudar a funcao derivada
    fx = funcaoDerivada(x)
    if fx == 0:
        return 0
    
    divisao = funcaoDerivada(x) / (math.factorial(len(listx)))
    listToResult = []

    for i in listx:
        listToResult.append(x - i)

    return multiVetor(listToResult) * divisao