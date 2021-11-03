'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if (n > 1):
    for i in range(2, int(n / 2) + 1):
      if (n % i == 0):
        print("Numarul", n, "nu este prim")
        break
    else:
      print("Numarul", n, "este prim")
  else:
    print("Numarul", n, "nu este prim")


'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p = 1
  for x in lst:
    p *= x
  return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if (x < y):
    a = x
    x = y
    y = a
  while (y):
    a = x % y
    x = y
    y = a
  return x

def show_menu():
  print("""
1. Să se stabilească daca un număr n este prim sau nu.
Exemplu: n = 3  este prim, dar n = 6 nu este prim
2. Să se calculeze produsul a n numere naturale
Exemplu: n = 3 și numerele 3, 4, 5, produsul este 60.
3. Să se calculeze CMMDC a 2 numere folosind doi algoritmi distincți.
Apasati X pentru a iesi din meniu.
""")
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while (x != y):
      if (x > y):
        x = x - y
      else:
        y = y - x
    return x


def main():
  while True:
    show_menu()
    P=input("Selecteaza problema: ")
    if(P=='1'):
      print("Ai ales problema 1")
      n=int(input("Numarul citit este: "))
      print(is_prime(n))
    elif(P=='2'):
      print("Ai ales problema 2")
      n=int(input("Numarul de elemente citite este: "))
      lst = []
      print("Numere care se citesc sunt:")
      for i in range (0,n):
        ele = int(input())
        lst.append(ele)
      print("Produsul numerelor din lista este:", get_product(lst))
    elif(P=='3'):
      print('''
Ai ales problema 3.
1. CMMDC V1
2. CMMDC V2 
''')
      P1 = input("Selecteaza varianta de rezolvare: ")
      if(P1 == '1'):
        x = int(input("Primul element citit este: "))
        y = int(input("Al doilea element citit este: "))
        print("Cel mai mare divizor comun ale lui", x, "si", y, "este", get_cmmdc_v1(x, y))
      elif(P1 == '2'):
        x = int(input())
        y = int(input())
        print("Cel mai mare divizor comun ale lui", x, "si", y, "este", get_cmmdc_v2(x, y))
      else:
        print("Comanda invalida. Reincearca")
    elif(P == 'X'):
      print("Ati iesit din meniu.")
      break
    else:
      print("Comanda invalida. Reincearca")
if __name__ == '__main__':
  main()
