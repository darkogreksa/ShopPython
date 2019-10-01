'''
Created on Jun 27, 2019

@author: Nemandza
'''
from cuvanje.citanje_iz_fajla import citanje_artikli, citanje_police, \
    citanje_stavke
from model.Klase import Stavka
from cuvanje.pisanje_u_fajl import pisanje_stavke


def prikaz_stavki():
    
    '''
    Funkcija za prikaz stavki, 
    ucitava sve stavke iz fajla i prikazuje ih na ekran
    '''
        
    stavke = []
    stavke = citanje_stavke()
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for i in stavke:
        print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(i.oznaka, i.kolicina, i.ukupna_cena, i.artikal, i.racun))
        print ("-"*br)
        
def dodavanje_stavki():
    
    '''
    Funkcija za dodavanje stavki, 
    preuzima od korisnika potrebne podatke za novu stavku,
    pravi je, smesta u listu i upisuje u fajl
    '''
    
    try:
        stavke = []
        stavke = citanje_stavke()
        oznaka = input("Unesite oznaku stavke: ")
        kolicina = float(input("Unesite kolicinu stavke: "))
        ukupna_cena = float(input("Unesite ukupnu cenu stavke: "))
        artikal = input("Unesite  artikal: ")
        racun = input("Unesite racun: ")
        s = Stavka(oznaka, kolicina, ukupna_cena, artikal, racun)
        
        '''a JE OBJEKAT KLASE SEKCIJA, 
        Artikal(oznaka, naziv, opis, cena, rok_trajanja) - konstruktor klase Artikal'''
        
        stavke.append(s)
        pisanje_stavke(stavke)
        print("Uspesno ste dodali artikal")
    except Exception as e:
        print(e)
        
def izmena_stavki():
    '''
    Funkcija za izmenu stavki, 
    pruza mogucnost izmene odredjenog parametra stavki
    '''
    try:
        stavke = []
        stavke = citanje_stavke()
        oznaka = input("Unesite oznaku za stavku koju zelite da izmenite: ")
        for i in stavke:
            if oznaka == i.oznaka:
                izmena = i
                print("Pronadjena oznaka")
                print()
                print("\nParametri za  menjanje:\n1 - Oznaka\n2 - Kolicina\n3 - Ukupna cena\n4 - Artikal\n5 - Racun")
                izbor = "0"
                izbor = input("Izaberite opciju: ")
                while izbor.upper() not in ("1","2","3","4","5"):
                    print("\nUneli ste pogresnu opciju.\n")
                    izbor = input("Izaberite opciju: ")
                if izbor == "1":
                    oznaka2 = input("Unesite oznaku za izmenu: ")
                    izmena.oznaka = oznaka2
                    pisanje_stavke(stavke)
                elif izbor == "2":
                    kolicina2 = float(input("Unesite kolicinu za izmenu: "))
                    izmena.kolicina = kolicina2
                    pisanje_stavke(stavke)
                elif izbor == "3":
                    ukupna_cena2 = float(input("Unesite ukupnu cenu za izmenu: "))
                    izmena.ukupna_cena = ukupna_cena2
                    pisanje_stavke(stavke)
                elif izbor == "4":
                    artikal2 = input("Unesite artikal za izmenu: ")
                    izmena.artikal = artikal2
                    pisanje_stavke(stavke)
                else:
                    racun2 = input("Unesite racun za izmenu: ")
                    izmena.racun = racun2
                    pisanje_stavke(stavke)
                    print("Uspesno ste odradili izmene")
                    return True
    except Exception as e:
        print(e)
        
def pretraga_stavki():
    '''
    Funkcija za pretragu stavki
    koja omogucava pretragu po odredjenom parametru
    '''
    try:
        stavke = []
        stavke = citanje_stavke()
        print("\nParametri za pretragu:\n1 - Oznaka\n2 - Kolicina\n3 - Ukupna cena\n4 - artikal\n5 - Racun")
        izbor = "0"
        izbor = input("Izaberite opciju: ")
        while izbor.upper() not in ("1", "2", "3", "4", "5"):
            print("\nUneli ste pogresnu opciju.\n")
            izbor = input("Izaberite opciju: ")
        if izbor == "1":
            oznaka2 = input("Unesite oznaku za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in stavke:
                if oznaka2 in p.oznaka:
                    print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
                    print ("-"*br)
        elif izbor == "2":
            kolicina2 = float(input("Unesite kolicinu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in stavke:
                if kolicina2 == p.kolicina:
                    print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
                    print ("-"*br)
        elif izbor == "3":
            ukupna_cena2 = float(input("Unesite ukupnu cenu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in stavke:
                if ukupna_cena2 == p.ukupna_cena:
                    print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
                    print ("-"*br)
        elif izbor == "4":
            artikal2 = input("Unesite artikal za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in stavke:
                if artikal2 in p.artikal:
                    print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
                    print ("-"*br)
        else:
            racun2 = float(input("Unesite racun za pretragu: "))
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in stavke:
                if racun2 == p.racun:
                    print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
                    print ("-"*br)
    except Exception as e:
        print(e)  

def sortiranje_stavki():
    '''
    Funkcija za sortiranje artikala po odredjenom parametru
    '''
    
    stavke = []
    stavke = citanje_stavke()
    print("Stavke sortirane po kolicini")
    
    stavke.sort(key=lambda x: x.kolicina, reverse=False)
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for p in stavke:
        print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(p.oznaka, p.kolicina, p.ukupna_cena, p.artikal, p.racun))
        print("-"*br)
