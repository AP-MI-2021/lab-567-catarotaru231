from Tests.run_tests import runalltests
from UI.consola import run_menu
from UI.consola2 import run_menu_2


def main():
    runalltests()
    optiune = input("Selectati consola 1 sau 2: ")
    while optiune != "1" and optiune != "2":
        print("Comanda invalida! Reincercati")
        optiune = input("Selectati consola 1 sau 2: ")
    if optiune == "1":
        run_menu([])
    else:
        run_menu_2([])
    run_menu([])


main()