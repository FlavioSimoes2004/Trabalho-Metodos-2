import DiferencasDivididas as DD
import Lagrange as L

def teste(x):
    #P pego do slide
    return 0.042 * (x**4) + 0.25 * (x**3) - 0.541 * (x**2) - 1.75 * x + 1

def main():
    print(L.getP(0.8, [0.0, 0.5, 1.0], [1.0, 0.6875, 0.0]))
    print(L.getErroTrunc(0.8, [0.0, 0.5, 1.0]))




main()