'''
Created on Jun 27, 2019

@author: Nemandza
'''
from cuvanje.citanje_iz_fajla import citanje_artikli, citanje_police, \
    citanje_racun, citanje_stavke
from model.Klase import Racun
from cuvanje.pisanje_u_fajl import pisanje_racun


def prikaz_racuna():
    
    '''
    Funkcija za prikaz racuna, 
    ucitava sve racune iz fajla i prikazuje ih na ekran
    '''
        
    racuni = []
    racuni = citanje_racun()
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for i in racuni:
        print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(i.oznaka, i.prodavac, i.ukupna_cena, i.datum))
        print ("-"*br)
        
def dodavanje_racuna():
    
    '''
    Funkcija za dodavanje racuna, 
    preuzima od korisnika potrebne podatke za novi racun,    
    pravi je, smesta u listu i upisuje u fajl
    '''
    
    try:
        racuni = []
        racuni = citanje_racun()
        oznaka = input("Unesite oznaku racuna: ")
        prodavac = input("Unesite prodavca racuna: ")
        ukupna_cena = float(input("Unesite ukupnu cenu racuna: "))
        datum = input("Unesite  datum racuna: ")
        r = Racun(oznaka, prodavac, ukupna_cena, datum)
        
        '''r JE OBJEKAT KLASE RACUN, 
        Racun(oznaka, prodavac, ukupna_cena, datum) - konstruktor klase Racun'''
        
        racuni.append(r)
        pisanje_racun(racuni)
        print("Uspesno ste dodali racun")
    except Exception as e:
        print(e)
        
def izmena_racuna():
    '''
    Funkcija za izmenu racuna, 
    pruza mogucnost izmene odredjenog parametra racuna
    '''
    try:
        racuni = []
        racuni = citanje_racun()
        oznaka = input("Unesite oznaku za racun koji zelite da izmenite: ")
        for i in racuni:
            if oznaka == i.oznaka:
                izmena = i
                print("Pronadjena oznaka")
                print()
                print("\nParametri za  menjanje:\n1 - Oznaka\n2 - Prodavac\n3 - Ukupna cena\n4 - Datum")
                izbor = "0"
                izbor = input("Izaberite opciju: ")
                while izbor.upper() not in ("1","2","3","4"):
                    print("\nUneli ste pogresnu opciju.\n")
                    izbor = input("Izaberite opciju: ")
                if izbor == "1":
                    oznaka2 = input("Unesite oznaku za izmenu: ")
                    izmena.oznaka = oznaka2
                    pisanje_racun(racuni)
                elif izbor == "2":
                    prodavac2 = input("Unesite prodavca za izmenu: ")
                    izmena.prodavac = prodavac2
                    pisanje_racun(racuni)
                elif izbor == "3":
                    ukupna_cena2 = float(input("Unesite ukupnu cenu za izmenu: "))
                    izmena.ukupna_cena = ukupna_cena2
                    pisanje_racun(racuni)
                else:
                    datum2 = input("Unesite datum za izmenu: ")
                    izmena.datum = datum2
                    pisanje_racun(racuni)
                    print("Uspesno ste odradili izmene")
                    return True
    except Exception as e:
        print(e)
        
def pretraga_racuna():
    '''
    Funkcija za pretragu racuna
    koja omogucava pretragu po odredjenom parametru
    '''
    try:
        racuni = []
        racuni = citanje_racun()
        print("\nParametri za pretragu:\n1 - Oznaka\n2 - Prodavac\n3 - Ukupna cena\n4 - Datum")
        izbor = "0"
        izbor = input("Izaberite opciju: ")
        while izbor.upper() not in ("1", "2", "3", "4"):
            print("\nUneli ste pogresnu opciju.\n")
            izbor = input("Izaberite opciju: ")
        if izbor == "1":
            oznaka2 = input("Unesite oznaku za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in racuni:
                if oznaka2 in p.oznaka:
                    print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
                    print ("-"*br)
        elif izbor == "2":
            prodavac2 = input("Unesite prodavca za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in racuni:
                if prodavac2 == p.prodavac:
                    print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
                    print ("-"*br)
        elif izbor == "3":
            ukupna_cena2 = float(input("Unesite ukupnu cenu za pretragu: "))
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in racuni:
                if ukupna_cena2 == p.ukupna_cena:
                    print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
                    print ("-"*br)
        else:
            datum2 = input("Unesite datum za pretragu: ")
            zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for p in racuni:
                if datum2 == p.datum:
                    print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
                    print ("-"*br)
    except Exception as e:
        print(e)  

def sortiranje_racuna():
    '''
    Funkcija za sortiranje racuna po odredjenom parametru
    '''
    
    racuni = []
    racuni = citanje_racun()
    print("\nParametri za  sortiranje:\n1 - Po ukupnoj ceni\n2 - Po datumu")
    izbor = "0"
    izbor = input("Izaberite opciju: ")
    while izbor.upper() not in ("1", "2"):
        print("\nUneli ste pogresnu opciju.\n")
        izbor = input("Izaberite opciju: ")
    if izbor == "1":
        racuni.sort(key=lambda x: x.ukupna_cena, reverse=False)
        zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
        br = len(zaglavlje)
        print ("-"*br)
        print(zaglavlje)
        print ("-"*br)
        for p in racuni:
            print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
            print("-"*br)
    else:
        racuni.sort(key=lambda x: x.datum, reverse=False)
        zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|".format("Oznaka", "Prodavac", "Ukupna cena", "Datum")
        br = len(zaglavlje)
        print ("-"*br)
        print(zaglavlje)
        print ("-"*br)
        for p in racuni:
            print("|{:<6s}|{:<12s}|{:<20.2f}|{:<20s}|".format(p.oznaka, p.prodavac, p.ukupna_cena, p.datum))
            print("-"*br)
            
def prikaz_stavki_i_artikala():
    '''
    Funkcija za prikaz svih stavki i artikala koje sadrze odgovarajuci racun,
    ona zahteva od korisnika da unese oznaku racuna
    i za taj racun  prikazuje na ekran sve stavke i artikle na koje se taj racun odnosi
    '''
    racuni = []
    stavke = []
    artikli = []
    
    racuni = citanje_racun()
    stavke = citanje_stavke()
    artikli = citanje_artikli()
    
    stavke_s = []
    artikli_a = []
    oznaka=input("Unesite oznaku racuna za prikaz stavki i artikala: ")
    
    for s in stavke:
        if oznaka == s.racun:
            stavke_s.append(s)
            
    for s in stavke:
        if oznaka == s.racun:
            for a in artikli:
                if s.artikal == a.oznaka:
                    artikli_a.append(a)

            
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|".format("Oznaka", "Kolicina", "Ukupna cena", "Artikal", "Racun")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for s in stavke_s:
        print("|{:<6s}|{:<12.2f}|{:<20.2f}|{:<20s}|{:<20s}|".format(s.oznaka, s.kolicina, s.ukupna_cena, s.artikal, s.racun))
        print("-"*br)
    
    zaglavlje = "|{:^6s}|{:^12s}|{:^20s}|{:^20s}|{:^20s}|{:^6s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Polica")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for a in artikli_a:
        print("|{:<6s}|{:<12s}|{:<20s}|{:<20.2f}|{:<20s}|{:^6s}|".format(a.oznaka, a.naziv, a.opis, a.cena, a.rok_trajanja, a.polica))
        print("-"*br)