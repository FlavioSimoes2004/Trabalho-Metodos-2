import DiferencasDivididas as DD
import Lagrange as L
import DiferencasFinitas as DF



def main():
    x = 1
    lx = []
    ly = []

    txt = '0 - fecha programa\n1 - lagrange\n2 - diferencas divididas\n3 - diferencas finitas'
    choice = 0
    while True:
        print(txt)
        choice = input()
        while choice < 0 or choice > 3:
            print('escolha invalida, digite novamente: ')
            choice = input()

        if choice == 0:
            break
        elif choice == 1:
            print("P = ", L.getP(x, lx, ly))
            print("erro truncamento = ", L.getErroTrunc(x, lx))
        elif choice == 2:
            print("P = ", DD.getP(x, lx, ly))
            print("erro truncamento = ", DD.getErroTrunc(x, lx))
        else:
            print("P = ", DF.getP(x, lx, ly))
            print("erro truncamento = ", DF.getEt(x, lx))
        



main()