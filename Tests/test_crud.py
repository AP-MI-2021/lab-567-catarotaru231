from Logic.crud import add_obiect, delete_obiect, modify_obiect
from Domain.obiect import create_obiect, get_id, get_nume,  get_descriere, get_pret_achizitie, get_locatie

def test_add_obiect():
    obiect = []
    obiect_adaugat = create_obiect('111a', 'birou', 'alb', 120.99, 'etaj')
    add_obiect(obiect, '111a', 'birou', 'alb', 120.99, 'etaj')
    assert obiect_adaugat == obiect[0]
    assert len(obiect) == 1
    assert get_id(obiect[0]) == '111a'
    assert get_nume(obiect[0]) == 'birou'
    assert get_descriere(obiect[0]) == 'alb'
    assert get_pret_achizitie(obiect[0]) == 120.99
    assert get_locatie(obiect[0]) == 'etaj'

    add_obiect(obiect, '112a', 'dulap', 'maro', 300.01, 'Cluj')
    obiect_adaugat_2 = create_obiect('112a', 'dulap', 'maro', 300.01, 'Cluj')
    assert len(obiect) == 2
    assert obiect[0] == obiect_adaugat
    assert obiect[1] == obiect_adaugat_2

def test_delete_obiect():
    obiect = []
    add_obiect(obiect, '101', 'masa', 'de lemn', 150, 'Iasi')

    delete_obiect('101', obiect)
    assert len(obiect) == 1
    add_obiect(obiect, '111', 'cutii', 'cu instrumente', 250, 'Etaj')
    add_obiect(obiect, '112', 'calculator', 'performant', 1000.89, 'Emag')
    delete_obiect('111', obiect)
    delete_obiect('112', obiect)

def test_modify_obiect():
    obiect = []
    obiect_modificat = create_obiect('112a', 'dulap', 'maro', 300.01, 'Cluj')
    add_obiect(obiect, '112a', 'dulap', 'maro', 300.01, 'Cluj')
    modify_obiect(obiect, '112a', 'dulap', 'maro', 300.01, 'Cluj')



