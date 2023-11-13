def funcao(x):
    return x ** 2


def getDiferencas(list):
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
    return calcInter(list2, ordem) - calcInter(list1, ordem) / divisao



def getDiferencas2(listx, ly):
    global listy
    listy = list.copy(ly)

    newMatrix = []
    n = listx.__len__()

    for i in range(n):
        print(i)
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
    return calcInter2(listx, list2, ordem) - calcInter2(listx, list1, ordem) / divisao