'''
Created on 21.06.2019.

@author: Greksa
'''
from cuvanje.citanje_iz_fajla import citanje_sekcije, citanje_police,\
    citanje_artikli
from model.Klase import Sekcija
from cuvanje.pisanje_u_fajl import pisanje_sekcija

def prikaz_sekcije():
    '''
    Funkcija za prikaz sekcije, 
    ucitava sve sekcije iz fajla i prikazuje ih na ekran
    '''
    sekcije = []
    sekcije = citanje_sekcije()
    zaglavlje = "|{:^6s}|{:^15s}|{:^20s}|{:^20s}|".format("Oznaka", "Naziv", "Opis", "Pozicija")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for s in sekcije:
        print("|{:<6s}|{:<15s}|{:<20s}|{:<20s}|".format(s.oznaka, s.naziv, s.opis, s.pozicija))
        print ("-"*br)
        
def dodavanje_sekcije():
    '''
    Funkcija za dodavanje sekcije, 
    preuzima od korisnika potrebne podatke za novu sekciju,
    pravi je, smesta u listu i upisuje u fajl
    '''
    try:
        sekcije = []
        sekcije = citanje_sekcije()
        oznaka = input("Unesite oznaku sekcije: ")
        naziv = input("Unesite naziv sekcije: ")
        opis = input("Unesite opis sekcije: ")
        pozicija = input("Unesite poziciju sekcije: ")  
        s = Sekcija(oznaka, naziv, opis, pozicija)
        
        '''S JE OBJEKAT KLASE SEKCIJA, 
        Sekcija(oznaka, naziv, opis, pozicija) - konstruktor klase Sekcija'''
        
        sekcije.append(s)
        pisanje_sekcija(sekcije)
        print("Uspesno ste dodali sekciju")
    except Exception as e:
        print(e)
        
def izmena_sekcije():
    '''
    Funkcija za izmenu sekcije, 
    pruza mogucnost izmene odredjenog parametra sekcije
    '''
    try:
        sekcije = []
        sekcije = citanje_sekcije()
        oznaka = input("Unesite oznaku sekcije koju zelite da izmenite: ")
        for i in sekcije:
            if oznaka == i.oznaka:
                izmena = i
                print("Pronadjena oznaka")
                print()
                print("\nParametri za  menjanje:\n1 - Oznaka\n2 - Naziv\n3 - Opis\n4 - Pozicija")
                izbor = "0"
                izbor = input("Izaberite opciju: ")
                while izbor.upper() not in ("1", "2", "3", "4"):
                    print("\nUneli ste pogresnu opciju.\n")
                    izbor = input("Izaberite opciju: ")
                if izbor == "1":
                    oznaka2 = input("Unesite oznaku za izmenu: ")
                    izmena.oznaka = oznaka2
                    pisanje_sekcija(sekcije)
                elif izbor == "2":
                    naziv2 = input("Unesite naziv za izmenu: ")
                    izmena.naziv = naziv2
                    pisanje_sekcija(sekcije)
                elif izbor == "3":
                    opis2 = input("Unesite opis za izmenu: ")
                    izmena.opis = opis2
                    pisanje_sekcija(sekcije)
                else:
                    pozicija2 = input("Unesite poziciju za izmenu: ")
                    izmena.pozicija = pozicija2
                    pisanje_sekcija(sekcije)
                    print("Uspesno ste odradili izmene")
                    return True
    except Exception as e:
        print(e)
        
def pretraga_sekcije():
    '''
    Funkcija za pretragu sekcija 
    koja omogucava pretragu po odredjenom parametru
    '''
    try:
        sekcije = []
        sekcije = citanje_sekcije()
        print("\nParametri za pretragu:\n1 - Oznaka\n2 - Naziv\n3 - Opis\n4 - Pozicija")
        izbor = "0"
        izbor = input("Izaberite opciju: ")
        while izbor.upper() not in ("1", "2", "3", "4"):
            print("\nUneli ste pogresnu opciju.\n")
            izbor = input("Izaberite opciju: ")
        if izbor == "1":
            oznaka2 = input("Unesite oznaku za pretragu: ")
            zaglavlje = "|{:^6s}|{:^15s}|{:^20s}|{:^20s}|".format("Oznaka", "Naziv", "Opis", "Pozicija")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for s in sekcije:
                if oznaka2 in s.oznaka:
                    print("|{:<6s}|{:<15s}|{:<20s}|{:<20s}|".format(s.oznaka, s.naziv, s.opis, s.pozicija))
                    print ("-"*br)
        elif izbor == "2":
            naziv2 = input("Unesite naziv za pretragu: ")
            zaglavlje = "|{:^6s}|{:^15s}|{:^20s}|{:^20s}|".format("Oznaka", "Naziv", "Opis", "Pozicija")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for s in sekcije:
                if naziv2.upper() in s.naziv.upper():
                    print("|{:<6s}|{:<15s}|{:<20s}|{:<20s}|".format(s.oznaka, s.naziv, s.opis, s.pozicija))
                    print ("-"*br)
        elif izbor == "3":
            opis2 = input("Unesite opis za pretragu: ")
            zaglavlje = "|{:^6s}|{:^15s}|{:^20s}|{:^20s}|".format("Oznaka", "Naziv", "Opis", "Pozicija")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for s in sekcije:
                if opis2.upper() in s.opis.upper():
                    print("|{:<6s}|{:<15s}|{:<20s}|{:<20s}|".format(s.oznaka, s.naziv, s.opis, s.pozicija))
                    print ("-"*br)
        else:
            pozicija2 = input("Unesite poziciju za pretragu: ")
            zaglavlje = "|{:^6s}|{:^15s}|{:^20s}|{:^20s}|".format("Oznaka", "Naziv", "Opis", "Pozicija")
            br = len(zaglavlje)
            print ("-"*br)
            print(zaglavlje)
            print ("-"*br)
            for s in sekcije:
                if pozicija2.upper() in s.pozicija.upper():
                    print("|{:<6s}|{:<15s}|{:<20s}|{:<20s}|".format(s.oznaka, s.naziv, s.opis, s.pozicija))
                    print ("-"*br)
    except Exception as e:
        print(e)  
        
def prikaz_polica_i_artikala():
    '''
    Funkcija za prikaz svih polica i artikala u sekciji,
    ona zahteva od korisnika da unese oznaku sekcije
    i za tu sekciju  prikazuje na ekran sve police i artikle koja se nalaze u njoj
    '''
    sekcije = []
    police = []
    artikli = []
    
    sekcije = citanje_sekcije()
    police = citanje_police()
    artikli = citanje_artikli()
    
    delovi_p = []
    delovi_a = []
    oznaka=input("Unesite oznaku sekcije za prikaz polica i artikala u njoj: ")
    
    for p in police:
        if oznaka == p.sekcija:
            delovi_p.append(p)
            
    for p in police:
        if oznaka == p.sekcija:
            for a in artikli:
                if p.oznaka == a.polica:
                    delovi_a.append(a)

            
    zaglavlje = "|{:^6s}|{:^6s}|{:^6s}|{:^20s}|{:^7s}|{:^7s}|{:^7s}|{:^8s}|".format("Oznaka", "Red","Kolona","Pozicija","Duzina","Sirina","Visina", "Oznaka S")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for ddp in delovi_p:
        print("|{:<6s}|{:<6d}|{:<6d}|{:^20s}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:^8s}|".format(ddp.oznaka, ddp.red, ddp.kolona, ddp.pozicija, ddp.duzina, ddp.sirina, ddp.visina, ddp.sekcija))
        print("-"*br)
    
    zaglavlje = "|{:^6s}|{:^20s}|{:^20s}|{:^7s}|{:^18s}|{:^8s}|".format("Oznaka", "Naziv", "Opis", "Cena", "Rok trajanja", "Oznaka P")
    br = len(zaglavlje)
    print ("-"*br)
    print(zaglavlje)
    print ("-"*br)
    for da in delovi_a:
        print("|{:<6s}|{:<20s}|{:^20s}|{:<7.2f}|{:^18s}|{:^8s}|".format(da.oznaka, da.naziv, da.opis, da.cena, da.rok_trajanja , da.polica))
        print("-"*br)