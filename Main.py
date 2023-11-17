import DiferencasDivididas as DD
import Lagrange as L
import DiferencasFinitas as DF



def main():
    print(DF.getOrdem([1.2, 1.4, 1.6, 1.8], [1.340, 1.678, 1.876, 2.242]))
    print(DF.getP(1.0, [1.2, 1.4, 1.6, 1.8], [1.340, 1.678, 1.876, 2.242]))



main()