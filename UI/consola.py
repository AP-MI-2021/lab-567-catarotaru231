from Domain.obiect import to_str
from Logic.crud import add_obiect, modify_obiect, delete_obiect
from Logic.operatiuni import mutare_locatie, concatenare

def print_menu():

    print('''
    MENIU
    1. CRUD
    2. OPERATIUNI
    3. Undo/Redo
    x. Iesire
    ''')

def print_crud_menu():

    print('''
    MENIU Crud
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate obiectele
    5. Inapoi
    ''')

def print_operatiuni_meniu():

    print('''
    MENIU Operatiuni 
    1. Mutarea tuturor obiectelor dintr-o locație în alta.
    2. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    3. Determinarea celui mai mare preț pentru fiecare locație.
    4. Ordonarea obiectelor crescător după prețul de achiziție.
    5. Afișarea sumelor prețurilor pentru fiecare locație.
    6. Inapoi
    ''')


def run_crud_ui(obiect):

    '''

    :param obiect: lista de obiecte
    :return:
    '''

    def handle_show_all(obiect):

        '''

        Afisare lista de obiecte din memorie
        :param obiect: lista de obiecte
        :return:
        '''

        for x in obiect:
            print(to_str(x))

    def handle_add_obiect_ui(obiect):

        '''

        Adaugam un obiect citit de la tastatura in lista de obiecte
        :param obiect: lista de obiecte
        :return:
        '''

        id = input("ID-ul obiectului este: ")
        nume = input("Numele obiectului este: ")
        descriere = input("Descrierea obiectului este: ")
        pret_achizitie = float(input("Pretul achizitiei este: "))
        locatie = input("Locatia obiectului este: ")
        add_obiect(obiect, id, nume, descriere, pret_achizitie, locatie)
        print("Obiectul a fost adaugat cu succes!")

    def handle_modify_obiect_ui(obiect):

        id = input("Id-ul obiectului modificat este: ")
        nume = input("Noul nume al obiectului este: ")
        descriere = input("Noua descriere a obiectului este: ")
        pret_achizitie = int(input("Noul pret al obiectului este: "))
        locatie = input("Noua locatie a obiectului este: ")
        return modify_obiect(obiect, id, nume, descriere, pret_achizitie, locatie)


    def handle_delete_obiect_ui(obiect):

        id = input("Id-ul obiectului de sters este: ")
        return delete_obiect(id, obiect)


    while True:
        print_crud_menu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_obiect_ui(obiect)
        elif cmd == '2':
            obiect = handle_modify_obiect_ui(obiect)
            print("Ati modificat obiectul cu id-ul", id, "cu succes!")
        elif cmd == '3':
            obiect = handle_delete_obiect_ui(obiect)
            print("Obiectul a fost sters cu succes!")
        elif cmd == '4':
            handle_show_all(obiect)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida.")


def run_operatiuni_ui(obiect):

    '''

    :param obiect: lista de obiecte
    :return:
    '''

    def handle_mutare_locatie(obiect):

        '''

        Mutarea tuturor obiectelor dintr-o locație în alta.
        :param obiect: lista de obiecte
        :return: lista initiala, cu locatia modificata cand se iveste cazul
        '''

        locatie_initiala = input("Selectati locatia din care va avea loc mutarea: ")
        locatie_finala = input("Selectati locatia in care va avea loc mutarea: ")
        return mutare_locatie(obiect, locatie_initiala, locatie_finala)

    def handle_concatenare(obiect):

        '''

        Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
        :param obiect: lista de obiecte
        :return: lista de obiecte cu date modificate
        '''

        pret = float(input("Valoarea citita este: "))
        sir_concatenat = input("String-ul citit este: ")
        return concatenare(obiect, pret, sir_concatenat)


    def handle_pret_max_locatie(obiect):
        pass

    def handle_sort_achizitie(obiect):
        pass

    def handle_show_pret_locatie(obiect):
        pass

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            obiect = handle_mutare_locatie(obiect)
        elif cmd == '2':
            obiect = handle_concatenare(obiect)
        elif cmd == '3':
            obiect = handle_pret_max_locatie(obiect)
        elif cmd == '4':
            obiect = handle_sort_achizitie(obiect)
        elif cmd == '5':
            obiect = handle_show_pret_locatie(obiect)
        elif cmd == '6':
            break
        else:
            print("Comanda invalida.")



def run_undo_redo_ui(obiect):
    pass

def run_console(obiect):

    '''

    :param obiect:
    :return:
    '''

    while True:
        print_menu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(obiect)
        elif cmd == '2':
            run_operatiuni_ui(obiect)
        elif cmd == '3':
            run_undo_redo_ui(obiect)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida.")
