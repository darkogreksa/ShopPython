'''
Created on 21.06.2019.

@author: Greksa
'''
from cuvanje.citanje_iz_fajla import citanje_police, citanje_artikli
from builtins import int
from model.Klase import Polica
from cuvanje.pisanje_u_fajl import pisanje_police

def prikaz_polica():
    '''
    Funkcija za prikaz polica, 
    ucitava sve police iz fajla i prikazuje ih na ekran
    '''
    police = []
    police = citanje_police()
    zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for p in police:
        print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
        print ("-"*br)
        
def dodavanje_police():
    '''
    Funkcija za dodavanje police, 
    preuzima od korisnika potrebne podatke za novu policu,
    pravi je, smesta u listu i upisuje u fajl
    '''
    try:
        police = []
        police = citanje_police()
        oznaka = input("Unesite oznaku sekcije: ")
        red = int(input("Unesite oznaku reda: "))
        kolona = int(input("Unesite oznaku kolone: "))
        pozicija = input("Unesite poziciju sekcije: ")
        duzina = float(input("Unesite duzinu: "))
        sirina = float(input("Unesite sirinu: "))
        visina = float(input("Unesite visinu: "))
        sekcija = input("Unesite oznaku sekcije kojoj polica pripada: ")  
        p = Polica(oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija)
        
        '''P JE OBJEKAT KLASE POLICA, 
        Polica(oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija) - konstruktor klase Polica'''
        
        police.append(p)
        pisanje_police(police)
        print("Uspesno ste dodali policu")
    except Exception as e:
        print(e)
        
def izmena_police():
    '''
    Funkcija za izmenu police, 
    pruza mogucnost izmene odredjenog parametra police
    '''
    try:
        police = []
        police = citanje_police()
        oznaka = input("Unesite oznaku police koju zelite da izmenite: ")
        for i in police:
            if oznaka == i.oznaka:
                izmena = i
                print("Pronadjena oznaka")
                print()
                print("\nParametri za  menjanje:\n1 - Oznaka\n2 - Red\n3 - Kolona\n4 - Pozicija\n5 - Duzina\n6 - Sirina\n7 - Visina\n8 - Oznaka sekcije")
                izbor = "0"
                izbor = input("Izaberite opciju: ")
                while izbor.upper() not in ("1","2","3","4","5","6","7","8"):
                    print("\nUneli ste pogresnu opciju.\n")
                    izbor = input("Izaberite opciju: ")
                if izbor == "1":
                    oznaka2 = input("Unesite oznaku za izmenu: ")
                    izmena.oznaka = oznaka2
                    pisanje_police(police)
                elif izbor == "2":
                    red2 = int(input("Unesite red za izmenu: "))
                    izmena.red = red2
                    pisanje_police(police)
                elif izbor == "3":
                    kolona2 = int(input("Unesite kolonu za izmenu: "))
                    izmena.kolona = kolona2
                    pisanje_police(police)
                elif izbor == "4":
                    pozicija2 = input("Unesite poziciju za izmenu: ")
                    izmena.pozicija = pozicija2
                    pisanje_police(police)
                elif izbor == "5":
                    duzina2 = float(input("Unesite duzinu za izmenu: "))
                    izmena.duzina = duzina2
                    pisanje_police(police)
                elif izbor == "6":
                    sirina2 = float(input("Unesite sirinu za izmenu: "))
                    izmena.sirina = sirina2
                    pisanje_police(police)
                elif izbor == "7":
                    visina2 = float(input("Unesite visinu za izmenu: "))
                    izmena.visina = visina2
                    pisanje_police(police)
                else:
                    sekcija2 = input("Unesite oznaku sekcije za izmenu: ")
                    izmena.sekcija = sekcija2
                    pisanje_police(police)
                    print("Uspesno ste odradili izmene")
                    return True
    except Exception as e:
        print(e)
        
def pretraga_police():
    '''
    Funkcija za pretragu polica 
    koja omogucava pretragu po odredjenom parametru
    '''
    try:
        police = []
        police = citanje_police()
        print("\nParametri za pretragu:\n1 - Oznaka\n2 - Red\n3 - Kolona\n4 - Pozicija\n5 - Duzina\n6 - Sirina\n7 - Visina")
        izbor = "0"
        izbor = input("Izaberite opciju: ")
        while izbor.upper() not in ("1", "2", "3", "4", "5", "6", "7"):
            print("\nUneli ste pogresnu opciju.\n")
            izbor = input("Izaberite opciju: ")
        if izbor == "1":
            oznaka2 = input("Unesite oznaku za pretragu: ")
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if oznaka2 in p.oznaka:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        elif izbor == "2":
            red2 = int(input("Unesite red za pretragu: "))
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if red2 == p.red:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        elif izbor == "3":
            kolona2 = int(input("Unesite kolonu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if kolona2 == p.kolona:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        elif izbor == "4":
            pozicija2 = input("Unesite poziciju za pretragu: ")
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if pozicija2 in p.pozicija:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        elif izbor == "5":
            duzina2 = float(input("Unesite duzinu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if duzina2 == p.duzina:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        elif izbor == "6":
            sirina2 = float(input("Unesite sirinu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if sirina2 == p.sirina:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
        else:
            visina2 = float(input("Unesite visinu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in police:
                if visina2 == p.visina:
                    print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
                    print ("-"*br)
    except Exception as e:
        print(e)  
        
def sortiranje_polica():
    '''
    Funkcija za sortiranje polica po odredjenom parametru
    '''
    
    police = []
    police = citanje_police()
    print("Police sortirane po poziciji")
    
    police.sort(key=lambda x: x.pozicija, reverse=False)
    zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^20s}|".format("Oznaka", "Red", "Kolona", "Pozicija", "Duzina", "Sirina", "Visina", "Oznaka sekcije")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for p in police:
        print("|{:<6s}|{:<6d}|{:<6d}|{:<20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<20s}|".format(p.oznaka, p.red, p.kolona, p.pozicija, p.duzina, p.sirina, p.visina, p.sekcija))
        print("-"*br)
        
def prikaz_artikala_za_police():
    '''
    Funkcija za prikaz svih artikala na odredjenoj polici,
    ona zahteva od korisnika da unese oznaku police
    i za tu policu  prikazuje na ekran sve artikle koji se nalaze na njoj
    '''
    police = []
    artikli = []
    
    police = citanje_police()
    artikli = citanje_artikli()
    
    artikli_a = []
    oznaka=input("Unesite oznaku police za prikaz artikala na njoj: ")
    
    for a in artikli:
        if oznaka == a.polica:
            artikli_a.append(a)
            
    zaglavlje = "|{:^6s}|{:^20s}|{:^20s}|{:^7s}|{:^18s}|{:^8s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Oznaka P")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for da in artikli_a:
        print("|{:<6s}|{:<20s}|{:^20s}|{:<7.2f}|{:^18s}|{:^8s}|".format(da.oznaka, da.naziv, da.opis, da.cena, da.rok_trajanja , da.polica))
        print("-"*br)