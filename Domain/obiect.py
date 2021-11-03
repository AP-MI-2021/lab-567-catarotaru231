def create_obiect(id, nume, descriere , pret_achizitie, locatie):

    '''

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: int
    :param locatie: string
    :return: Dict
    '''

    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret_achizitie": pret_achizitie,
        "locatie": locatie
    }

def get_id(obiect):

    '''

    :param obiect:
    :return: id - string
    '''

    return obiect['id']

def get_nume(obiect):

    '''

    :param obiect:
    :return: nume - string
    '''

    return obiect['nume']

def get_descriere(obiect):

    '''

    :param obiect:
    :return: descriere - string
    '''

    return obiect['descriere']

def get_pret_achizitie(obiect):

    '''

    :param obiect:
    :return: pret_achizitie - float
    '''

    return obiect['pret_achizitie']

def get_locatie(obiect):

    '''

    :param obiect:
    :return: locatie - string
    '''

    return obiect['locatie']

def to_str(obiect):

    return f'ID={get_id(obiect)}, nume={get_nume(obiect)}, descriere={get_descriere(obiect)}, pret_achizitie={get_pret_achizitie(obiect)}, locatie={get_locatie(obiect)}'
