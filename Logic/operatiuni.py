from Domain.obiect import create_obiect, get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie

def mutare_locatie(obiect, locatie_initiala,locatie_finala):

    '''

    Mutarea tuturor obiectelor dintr-o locație în alta.
    :param obiect: lista de obiecte
    :param locatie_initiala: string cu locatia initiala
    :param locatie_finala: string cu locatia dorita
    :return: obiect_nou: lista initiala, cu locatia modificata cand se iveste cazul
    '''

    obiect_nou = []
    for x in obiect:
        if(get_locatie(x) == locatie_initiala):
            x_nou = create_obiect(get_id(x),get_nume(x),get_descriere(x),get_pret_achizitie(x),locatie_finala)
            obiect_nou.append(x_nou)
        else:
            obiect_nou.append(x)
    return obiect_nou

def concatenare(obiect, pret, sir_concatenat):

    '''

    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param obiect: lista de obiecte
    :param pret: valoarea limita minima ceruta
    :param sir_concatenat: sirul ce trebuie adaugat la descriere
    :return: lista de obiecte cu datele modificate
    '''

    obiect_nou = []
    for x in obiect:
        if get_pret_achizitie(x) > pret:
            descriere_noua = get_descriere(x) + " " + sir_concatenat
            x_nou = create_obiect(get_id(x), get_nume(x), descriere_noua, get_pret_achizitie(x), get_locatie(x))
            obiect_nou.append(x_nou)
        else:
            obiect_nou.append(x)
    return obiect_nou
