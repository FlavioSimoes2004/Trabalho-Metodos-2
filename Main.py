import DiferencasDivididas as DD

def teste(x):
    #P pego do slide
    return 0.042 * (x**4) + 0.25 * (x**3) - 0.541 * (x**2) - 1.75 * x + 1

def main():
    #print(DD.getOrdem2([-2, -1, 0, 1, 2], [1, 2, 1, -1, -2]))
    print(teste(1))
    print(DD.getP(1.0, [-2, -1, 0, 1, 2], [1, 2, 1, -1, -2]))




main()