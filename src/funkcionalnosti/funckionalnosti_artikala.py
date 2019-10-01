'''
Created on Jun 26, 2019

@author: Nemandza
'''
from cuvanje.citanje_iz_fajla import citanje_artikli, citanje_police, \
    citanje_sekcije
from model.Klase import Artikal
from cuvanje.pisanje_u_fajl import pisanje_artikli


def prikaz_artikla():
    
    '''
    Funkcija za prikaz artikala, 
    ucitava sve artikle iz fajla i prikazuje ih na ekran
    '''
        
    artikli = []
    artikli = citanje_artikli()
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for i in artikli:
        print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(i.oznaka, i.naziv, i.opis, i.cena, i.rok_trajanja, i.polica))
        print ("-"*br)
        
def dodavanje_artikala():
    
    '''
    Funkcija za dodavanje artikala, 
    preuzima od korisnika potrebne podatke za novi artikal,
    pravi je, smesta u listu i upisuje u fajl
    '''
    
    try:
        artikli = []
        artikli = citanje_artikli()
        oznaka = input("Unesite oznaku artikla: ")
        naziv = input("Unesite naziv artikla: ")
        opis = input("Unesite opis artikla: ")
        cena = float(input("Unesite cenu: "))
        rok_trajanja = input("Unesite rok trajanja")
        polica = input("Unesite policu")
        a = Artikal(oznaka, naziv, opis, cena, rok_trajanja, polica);
        
        '''a JE OBJEKAT KLASE SEKCIJA, 
        Artikal(oznaka, naziv, opis, cena, rok_trajanja) - konstruktor klase Artikal'''
        
        artikli.append(a)
        pisanje_artikli(artikli)
        print("Uspesno ste dodali artikal")
    except Exception as e:
        print(e)
def izmena_artikala():
    '''
    Funkcija za izmenu artikla, 
    pruza mogucnost izmene odredjenog parametra artikla
    '''
    try:
        artikli = []
        artikli = citanje_artikli()
        oznaka = input("Unesite oznaku artikla kojeg zelite da izmenite: ")
        for i in artikli:
            if oznaka == i.oznaka:
                izmena = i
                print("Pronadjena oznaka")
                print()
                print("\nParametri za  menjanje:\n1 - Oznaka\n2 - Naziv\n3 - Opis\n4 - Cena\n5 - Rok trajanja\n6 - Polica ")
                izbor = "0"
                izbor = input("Izaberite opciju: ")
                while izbor.upper() not in ("1","2","3","4","5","6"):
                    print("\nUneli ste pogresnu opciju.\n")
                    izbor = input("Izaberite opciju: ")
                if izbor == "1":
                    oznaka2 = input("Unesite oznaku za izmenu: ")
                    izmena.oznaka = oznaka2
                    pisanje_artikli(artikli)
                elif izbor == "2":
                    naziv2 = input("Unesite naziv za izmenu: ")
                    izmena.naziv = naziv2
                    pisanje_artikli(artikli)
                elif izbor == "3":
                    opis2 = input("Unesite opis za izmenu: ")
                    izmena.opis = opis2
                    pisanje_artikli(artikli)
                elif izbor == "4":
                    cena2 = float(input("Unesite cenu za izmenu: "))
                    izmena.cena = cena2
                    pisanje_artikli(artikli)
                elif izbor == "5":
                    rok_trajanja2 = input("Unesite rok trajanja za izmenu: ")
                    izmena.rok_trajanja = rok_trajanja2
                    pisanje_artikli(artikli)     
                else:
                    polica2 = input("Unesite policu za izmenu: ")
                    izmena.polica = polica2
                    pisanje_artikli(artikli)
                    print("Uspesno ste odradili izmene")
                    return True
    except Exception as e:
        print(e)
        
def pretraga_artikala():
    '''
    Funkcija za pretragu artikala 
    koja omogucava pretragu po odredjenom parametru
    '''
    try:
        artikli = []
        artikli = citanje_artikli()
        print("\nParametri za pretragu:\n1 - Oznaka\n2 - Naziv\n3 - Opis\n4 - Cena\n5 - Rok trajanja")
        izbor = "0"
        izbor = input("Izaberite opciju: ")
        while izbor.upper() not in ("1", "2", "3", "4", "5"):
            print("\nUneli ste pogresnu opciju.\n")
            izbor = input("Izaberite opciju: ")
        if izbor == "1":
            oznaka2 = input("Unesite oznaku za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in artikli:
                if oznaka2 in p.oznaka:
                    print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(p.oznaka, p.naziv, p.opis, p.cena, p.rok_trajanja, p.polica))
                    print ("-"*br)
        elif izbor == "2":
            naziv2 = input("Unesite naziv za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in artikli:
                if naziv2 == p.naziv:
                    print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(p.oznaka, p.naziv, p.opis, p.cena, p.rok_trajanja, p.polica))
                    print ("-"*br)
        elif izbor == "3":
            opis2 = input("Unesite opis za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in artikli:
                if opis2 == p.opis:
                    print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(p.oznaka, p.naziv, p.opis, p.cena, p.rok_trajanja, p.polica))
                    print ("-"*br)
        elif izbor == "4":
            cena2 = float(input("Unesite cenu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in artikli:
                if cena2 == p.cena:
                    print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(p.oznaka, p.naziv, p.opis, p.cena, p.rok_trajanja, p.polica))
                    print ("-"*br)
        else:
            rok_trajanja2 = input("Unesite rok trajanja za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in artikli:
                if rok_trajanja2 == p.rok_trajanja:
                    print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(p.oznaka, p.naziv, p.opis, p.cena, p.rok_trajanja, p.polica))
                    print ("-"*br)
    except Exception as e:
        print(e)  

def sortiranje_artikala():
    '''
    Funkcija za sortiranje artikala po odredjenom parametru
    '''
    
    artikli = []
    artikli = citanje_artikli()
    print("\nParametri za  sortiranje:\n1 - Po ceni\n2 - Po roku trajanja")
    izbor = "0"
    izbor = input("Izaberite opciju: ")
    while izbor.upper() not in ("1", "2"):
        print("\nUneli ste pogresnu opciju.\n")
        izbor = input("Izaberite opciju: ")
    if izbor == "1":
        artikli.sort(key=lambda x: x.cena, reverse=False)
        zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^16s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
        br = len(zaglavlje)
        print ("-"*br)
        print(zaglavlje)
        print ("-"*br)
        for x in artikli:
            print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^16s}|".format(x.oznaka,x.naziv,x.opis,x.cena,x.rok_trajanja,x.polica))
            print("-"*br)
    else:
        artikli.sort(key=lambda x: x.rok_trajanja, reverse=False)
        zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^16s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
        br = len(zaglavlje)
        print ("-"*br)
        print(zaglavlje)
        print ("-"*br)
        for x in artikli:
            print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^16s}|".format(x.oznaka,x.naziv,x.opis,x.cena,x.rok_trajanja,x.polica))
            print("-"*br)