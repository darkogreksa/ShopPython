'''
Created on 21.06.2019.

@author: Greksa
'''
from funkcionalnosti.funkcionalnosti_sekcije import prikaz_sekcije,\
    dodavanje_sekcije, izmena_sekcije, pretraga_sekcije,\
    prikaz_polica_i_artikala
from funkcionalnosti.funkcionalnosti_police import prikaz_polica,\
    dodavanje_police, izmena_police, pretraga_police, sortiranje_polica,\
    prikaz_artikala_za_police
from funkcionalnosti.funckionalnosti_artikala import prikaz_artikla, \
    dodavanje_artikala, izmena_artikala, pretraga_artikala, \
    sortiranje_artikala
from funkcionalnosti.funkcionalnosti_stavki import prikaz_stavki, \
    dodavanje_stavki, izmena_stavki, pretraga_stavki, sortiranje_stavki
from funkcionalnosti.funkcionalnosti_racuna import prikaz_racuna, \
    dodavanje_racuna, izmena_racuna, pretraga_racuna, sortiranje_racuna,\
    prikaz_stavki_i_artikala
    
def glavni_meni():
    '''
    Glavni meni  koji omogucava korisniku da izabere rad sa ponudjenim opcijama
    '''
    print("Meni:\n ")
    print("1 - Rad sa sekcijama\n2 - Rad sa policama\n3 - Rad sa artiklima\n4 - Rad sa stavkama\n5 - Rad sa racunima\nX - Izlazak iz aplikacije ")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper()

def sekcije_meni():
    '''
    Meni za sekcije,koji pruza korisniku odredjene operacije sa sekcijama
    '''
    print()
    print("Izabrali ste rad sa sekcijama\n")
    print("""Ponudjene opcije:\n1 - Prikaz svih sekcija\n2 - Dodavanje sekcija\n3 - Izmena vrednosti sekcija
4 - Pretraga sekcija\n5 - Prikaz svih polica u sekciji i artikala na odgovarajucoj polici\nX - Povratak u glavni meni""")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper() 

def sekcije_izbor():
    '''
    Izbor opcije za sekcije koji poziva odredjenu funkciju za izabranu opciju
    '''
    opcija="0"
    while opcija !="X":
        opcija=sekcije_meni()
        if opcija=="1":
            prikaz_sekcije()
        elif opcija=="2":
            dodavanje_sekcije()
        elif opcija=="3":
            izmena_sekcije()
        elif opcija=="4":
            pretraga_sekcije()
        elif opcija=="5":
            prikaz_polica_i_artikala()

def police_meni():
    '''
    Meni za police,koji pruza korisniku odredjene operacije sa policama
    '''
    print()
    print("Izabrali ste rad sa policama\n")
    print("""Ponudjene opcije:\n1 - Prikaz svih polica\n2 - Dodavanje polica\n3 - Izmena vrednosti polica
4 - Pretraga polica\n5 - Prikaz svih polica sortiranih po poziciji\n6 - Prikaz svih artikala na odgovarajucoj polici\nX - Povratak u glavni meni""")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","6","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper() 

def police_izbor():
    '''
    Izbor opcije za police koji poziva odredjenu funkciju za izabranu opciju
    '''
    opcija="0"
    while opcija !="X":
        opcija=police_meni()
        if opcija=="1":
            prikaz_polica()
        elif opcija=="2":
            dodavanje_police()
        elif opcija=="3":
            izmena_police()
        elif opcija=="4":
            pretraga_police()
        elif opcija=="5":
            sortiranje_polica()
        elif opcija=="6":
            prikaz_artikala_za_police()

def artikli_meni():
    '''
    Meni za artikle,koji pruza korisniku odredjene operacije sa artiklima
    '''
    print()
    print("Izabrali ste rad sa artiklima\n")
    print("""Ponudjene opcije:\n1 - Prikaz svih artikala\n2 - Dodavanje artikala\n3 - Izmena vrednosti artikala
4 - Pretraga artikala\n5 - Sortiranje artikla\nX - Povratak u glavni meni""")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper() 

def artikli_izbor():
    '''
    Izbor opcije za artikle koji poziva odredjenu funkciju za izabranu opciju
    '''
    opcija="0"
    while opcija !="X":
        opcija=artikli_meni()
        if opcija=="1":
            prikaz_artikla()
        elif opcija=="2":
            dodavanje_artikala()
        elif opcija=="3":
            izmena_artikala()
        elif opcija=="4":
            pretraga_artikala()
        elif opcija=="5":
            sortiranje_artikala()
def stavke_meni():
    '''
    Meni za stavke,koji pruza korisniku odredjene operacije sa stavkama
    '''
    print()
    print("Izabrali ste rad sa stavkama\n")
    print("""Ponudjene opcije:\n1 - Prikaz svih stavki\n2 - Dodavanje stavke\n3 - Izmena vrednosti stavke
4 - Pretraga stavke\n5 - Sortiranje stavke po kolicini\nX - Povratak u glavni meni""")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper() 

def stavke_izbor():
    '''
    Izbor opcije za stavke koji poziva odredjenu funkciju za izabranu opciju
    '''
    opcija="0"
    while opcija !="X":
        opcija=stavke_meni()
        if opcija=="1":
            prikaz_stavki()
        elif opcija=="2":
            dodavanje_stavki()
        elif opcija=="3":
            izmena_stavki()
        elif opcija=="4":
            pretraga_stavki()
        elif opcija=="5":
            sortiranje_stavki()
            
def racuni_meni():
    '''
    Meni za racune,koji pruza korisniku odredjene operacije sa racunima
    '''
    print()
    print("Izabrali ste rad sa racunima\n")
    print("""Ponudjene opcije:\n1 - Prikaz svih racuna\n2 - Dodavanje racuna\n3 - Izmena vrednosti racuna
4 - Pretraga racuna\n5 - Sortiranje racuna\n6 - Prikaz stavki i artikala za racun\nX - Povratak u glavni meni""")
    opcija=input("Izaberite opciju: ")
    while opcija.upper() not in ("1","2","3","4","5","6","X"):
        print("\nUneli ste pogresu opciju.\n")
        opcija=input("Izaberite opciju: ")
    return opcija.upper() 

def racuni_izbor():
    '''
    Izbor opcije za stavke koji poziva odredjenu funkciju za izabranu opciju
    '''
    opcija="0"
    while opcija !="X":
        opcija=racuni_meni()
        if opcija=="1":
            prikaz_racuna()
        elif opcija=="2":
            dodavanje_racuna()
        elif opcija=="3":
            izmena_racuna()
        elif opcija=="4":
            pretraga_racuna()
        elif opcija=="5":
            sortiranje_racuna()
        elif opcija=="6":
            prikaz_stavki_i_artikala()