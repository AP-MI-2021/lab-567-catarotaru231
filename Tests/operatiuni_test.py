from Logic.operatiuni import mutare_locatie, concatenare
from Logic.crud import add_obiect
from Domain.obiect import get_locatie

def test_mutare_locatie():

    obiect = []
    add_obiect(obiect, 'id1', 'aparat de cafea', 'nou', 80, 'Iasi')
    add_obiect(obiect, 'id2', 'scaun', 'de piele', 75, 'Iasi')
    mutare_locatie(obiect, 'Iasi', 'Alba')
    assert get_locatie(obiect[0]) == 'Alba'
    assert get_locatie(obiect[1]) == 'Alba'