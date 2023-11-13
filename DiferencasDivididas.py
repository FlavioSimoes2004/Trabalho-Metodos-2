def funcao(x):
    return x ** 2


def getDiferencas(list):
    newMatrix = []
    n = list.__len__()

    for i in range(n):
        print(i)
        newMatrix.append(diferencas(list, i, False))
        
    return newMatrix



def diferencas(list, ordem, recursivo):
    n = list.__len__()
    listReturn = []

    if ordem == 0:
        if recursivo == False:
            for i in range(n):
                listReturn.append(funcao(list[i]))
            return listReturn
        else:
            print("seila")
    else:
        got = 0
        listRecursivo = []
        for i in range(n):
            listRecursivo.append(list[i])
            got += 1
            if i == n - 1:
                listReturn.append(diferencas(listRecursivo, (ordem - 1), True))
                break
            elif got == ordem + 1:
                listReturn.append(diferencas(listRecursivo, (ordem - 1), True))
                got = 0
                i-=1
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

    return calcInter(list2, ordem - 1) - calcInter(list1, ordem -1) / (list[list.__len__() - 1] - list[0])