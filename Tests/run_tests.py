from Tests.test_crud import test_adauga_obiect, test_sterge_obiect, test_modifica_obiect
from Tests.domain_test import test_obiect
from Tests.operatiuni_test import test_mutare_obiect_locatie, test_concatenare, test_pret_max_locatie, \
    test_ordonare_crescator_pret, test_suma_pret_locatie
from Tests.undo_redo_test import test_ui_undo_redo


def runalltests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_modifica_obiect()
    test_mutare_obiect_locatie()
    test_concatenare()
    test_pret_max_locatie()
    test_ordonare_crescator_pret()
    test_suma_pret_locatie()
    test_ui_undo_redo()