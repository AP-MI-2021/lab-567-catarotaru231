from Domain.obiect import create_obiect, get_descriere, get_locatie, get_id, get_pret_achizitie, get_nume

def add_obiect(obiect, id, nume, descriere, pret_achizitie, locatie):

    '''

    Adaugam in memorie, in lista de obiecte un obiect format din field-urile: id, nume, descriere, pret_achizitie, locatie
    :param obiect: lista de obiecte
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return:
    '''

    x = create_obiect(id, nume, descriere, pret_achizitie, locatie)
    obiect.append(x)

def modify_obiect(obiect, id, nume, descriere, pret_achizitie, locatie):

    '''

    Modifica atributele unui obiect dupa id-ul sau
    :param obiect:
    :param id:
    :param nume:
    :param descriere:
    :param pret_achizitie:
    :param locatie:
    :return:
    '''

    obiect_nou = []
    for x in obiect:
        if get_id(x) == id:
            x_nou = create_obiect(id, nume, descriere, pret_achizitie, locatie)
            obiect_nou.append(x_nou)
        else:
            obiect_nou.append(x)
    return obiect_nou

def delete_obiect(id, obiect):

    '''

    Sterge un obiect dupa id-ul sau
    :param id: string
    :param obiect: lista de obiecte
    :return: lista fara obiectul de sters
    '''

    return [x for x in obiect if get_id(x) != id]


