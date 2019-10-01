'''
Created on 20.06.2019.

@author: Greksa
'''
from io import open
from cuvanje.putanje import artikalFajl, sekcijeFajl, policeFajl, stavkeFajl,\
    racunFajl
from model.Klase import Artikal, Sekcija, Polica, Stavka, Racun

def citanje_artikli():
    '''
    Funkcija koja ucitava sve artikle iz fajla i smesta ih u listu
    '''
    artikli = []
    with open(artikalFajl, "r") as f:
        for linija in f:
            polja = linija.strip().split("|")
            oznaka = polja[0]
            naziv = polja[1]
            opis = polja[2]
            cena = float(polja[3])
            rok_trajanja = polja[4]
            polica = polja[5]
            artikli.append(Artikal(oznaka, naziv, opis, cena, rok_trajanja, polica))
    return artikli
    
def citanje_sekcije():
    '''
    Funkcija koja ucitava sve sekcije iz fajla i smesta ih u listu
    '''
    sekcije = []
    with open(sekcijeFajl, "r") as f:
        for linija in f:
            polja = linija.strip().split("|")
            oznaka = polja[0]
            naziv = polja[1]
            opis = polja[2]
            pozicija = polja[3]
            sekcije.append(Sekcija(oznaka, naziv, opis, pozicija))
    return sekcije

def citanje_police():
    '''
    Funkcija koja ucitava sve police iz fajla i smesta ih u listu
    '''
    police = []
    with open(policeFajl, "r") as f:
        for linija in f:
            polja = linija.strip().split("|")
            oznaka = polja[0]
            red = int(polja[1])
            kolona = int(polja[2])
            pozicija = polja[3]
            duzina = float(polja[4])
            sirina = float(polja[5])
            visina = float(polja[6])
            sekcija = polja[7]
            police.append(Polica(oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija))
    return police

def citanje_stavke():
    '''
    Funkcija koja ucitava sve stavke iz fajla i smesta ih u listu
    '''
    stavke = []
    with open(stavkeFajl, "r") as f:
        for linija in f:
            polja = linija.strip().split("|")
            oznaka = polja[0]
            kolicina = float(polja[1])
            ukupna_cena = float(polja[2])
            artikal = polja[3]
            racun = polja[4]
            stavke.append(Stavka(oznaka, kolicina, ukupna_cena, artikal, racun))
    return stavke

def citanje_racun():
    '''
    Funkcija koja ucitava sve racune iz fajla i smesta ih u listu
    '''
    racuni = []
    with open(racunFajl, "r") as f:
        for linija in f:
            polja = linija.strip().split("|")
            oznaka = polja[0]
            prodavac = polja[1]
            ukupna_cena = float(polja[2])
            datum = polja[3]
            racuni.append(Racun(oznaka, prodavac, ukupna_cena, datum))
    return racuni