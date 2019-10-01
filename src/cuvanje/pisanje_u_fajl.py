
from cuvanje.putanje import artikalFajl, sekcijeFajl, policeFajl, stavkeFajl,\
    racunFajl
    
def pisanje_artikli(artikal):

    with open(artikalFajl,"w") as f:
            for i in artikal:
                f.write("{}|".format(i.oznaka))
                f.write("{}|".format(i.naziv))
                f.write("{}|".format(i.opis))
                f.write("{}|".format(i.cena))
                f.write("{}|".format(i.rok_trajanja))
                f.write("{}|\n".format(i.polica))
                
def pisanje_sekcija(sekcija):

    with open(sekcijeFajl,"w")as f:
        for a in sekcija:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.naziv))
            f.write("{}|".format(a.opis))
            f.write("{}|\n".format(a.pozicija))
            
def pisanje_police(police):
   
    with open(policeFajl,"w") as f:
        for a in police:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.red))
            f.write("{}|".format(a.kolona))
            f.write("{}|".format(a.pozicija))
            f.write("{}|".format(a.duzina))
            f.write("{}|".format(a.sirina))
            f.write("{}|".format(a.visina))
            f.write("{}|\n".format(a.sekcija))
            
def pisanje_stavke(stavke):
   
    with open(stavkeFajl,"w") as f:
        for a in stavke:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.kolicina))
            f.write("{}|".format(a.ukupna_cena))
            f.write("{}|".format(a.artikal))
            f.write("{}|\n".format(a.racun))
            
def pisanje_racun(racun):
   
    with open(racunFajl,"w") as f:
        for a in racun:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.prodavac))
            f.write("{}|".format(a.ukupna_cena))
            f.write("{}|\n".format(a.datum))
