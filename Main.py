import DiferencasDivididas as DD
import Lagrange as L
import DiferencasFinitas as DF



def main():
    x = 1
    lx = [-2.0, -1.0, 0.0, 1.0, 2.0]
    ly = [1.0, 2.0, 1.0, -1.0, -2.0]

    txt = '0 - fecha programa\n1 - lagrange\n2 - diferencas divididas\n3 - diferencas finitas'
    choice = 0
    while True:
        print(txt)
        choice =  int(input())
        while choice < 0 or choice > 3:
            print('escolha invalida, digite novamente: ')
            choice = int(input())

        if choice == 0:
            break
        elif choice == 1:
            print("\nP = ", L.getP(x, lx, ly))
            print("erro truncamento = ", L.getErroTrunc(x, lx))
        elif choice == 2:
            print("\nORDEM = ", DD.getOrdem2(lx, ly))
            print("P = ", DD.getP(x, lx, ly))
            print("erro truncamento = ", DD.getErroTrunc(x, lx))
        else:
            print("\nORDEM = ", DF.getOrdem(lx, ly))
            print("P = ", DF.getP(x, lx, ly))
            print("erro truncamento = ", DF.getEt(x, lx))
        print("\n")
        



main()