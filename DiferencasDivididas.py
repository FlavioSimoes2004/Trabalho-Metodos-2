def funcao(x):
    return x ** 2

def getDiferencas(list):
    newMatrix = []
    n = list.__len__()

    for i in range(n):
        print(i)
        #newMatrix.append(diferencas(list, i))
        
    return newMatrix



def diferencas(list, ordem):
    n = list.__len__()
    newList = []

    init_pos = 0
    if ordem == 0:
        for i in range(n):
            newList.append(funcao(list[i]))
        return newList
    else:
