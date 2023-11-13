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

    return calcInter(list2, ordem - 1) - calcInter(list1, ordem - 1) / (list[list.__len__() - 1] - list[0])