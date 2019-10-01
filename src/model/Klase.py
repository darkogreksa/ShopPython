'''
Created on 17.06.2019.

@author: Greksa
'''


class Identifikacija(object):
    '''
    Klasa koja sadrzi atribute za identifikaciju 
    '''

    def __init__(self, oznaka, **kwargs):
        '''
        Konstruktor
        :param oznaka: cuva tekstualnu vrednost za oznaku
        '''
        """self je eksplicitan prvi parametar, ** koristimo kod visestrukog nasledjivanja
        kada nismo sigurni koliko cemo parametara proslediti"""
        
        super().__init__(**kwargs)
        self.oznaka = oznaka
    
    def __str__(self):
        '''
        Metoda vraca tekstualnu prezentaciju objekta
        '''
        return "{}".format(self.oznaka)


class Sekcija(Identifikacija):
    '''
    Klasa koja sadrzi atribute za sekciju 
    '''

    def __init__(self, oznaka, naziv, opis, pozicija):
        '''
        Konstruktor
        :param oznaka: cuva tekstualnu vrednost za oznaku
        :param naziv: cuva tekstualnu vrednost za naziv
        :param opis: cuva tekstualnu vrednost za opis
        :param pozicija: cuva tekstualnu vrednost za poziciju
        '''
        
        super().__init__(oznaka=oznaka)
        self.naziv = naziv
        self.opis = opis
        self.pozicija = pozicija
    
    def __str__(self):
        '''
        Metoda koja vraca tekstualnu prezentaciju za sekciju
        '''
        return"{} {} {} {}".format(super().__str__(), self.naziv, self.opis, self.pozicija)
    
    
class Polica(Identifikacija):
    '''
    Klasa koja sadrzi atribute za policu 
    '''

    def __init__(self, oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija):
        '''
        Konstruktor
        :param oznaka: cuva tekstualnu vrednost za oznaku
        :param red: cuva celobrojnu vrednost za red
        :param kolona: cuva celobrojnu vrednost za kolonu
        :param pozicija: cuva tekstualnu vrednost za poziciju
        :param duzina: cuva decimalnu vrednost za duzinu
        :param sirina: cuva decimalnu vrednost za sirinu
        :param visina: cuva decimalnu vrednost za visinu
        :param sekcija: cuva referencu na sekciju
        '''
        
        super().__init__(oznaka=oznaka)
        self.red = red
        self.kolona = kolona
        self.pozicija = pozicija
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.sekcija = sekcija
        
        "property je specijalni atribut koji dinamicki izracunava vrednost za pozvanu instancu"

    @property
    def red(self):
        '''
        Getter za vracane vrednosti reda
        '''
        return self.__red
    
    @red.setter
    def red(self, value):
        '''
        Setter za inicijalizovanje vrednosti reda
        
        :param value: vrednost koja se postavlja za red
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__red = value
        
    @property
    def kolona(self):
        '''
        Getter za vracane vrednosti kolone
        '''
        return self.__kolona
    
    @kolona.setter
    def kolona(self, value):
        '''
        Setter za inicijalizovanje vrednosti kolone
        
        :param value: vrednost koja se postavlja za red
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__kolona = value
        
    @property
    def duzina(self):
        '''
        Getter za vracane vrednosti duzine
        '''
        return self.__duzina
    
    @duzina.setter
    def duzina(self, value):
        '''
        Setter za inicijalizovanje vrednosti duzine
        
        :param value: vrednost koja se postavlja za duzinu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__duzina = value
   
    @property
    def sirina(self):
        '''
         Getter za vracane vrednosti sirine
        '''
        return self.__sirina
    
    @sirina.setter
    def sirina(self, value):
        '''
        Setter za inicijalizovanje vrednosti sirine
        
        :param value: vrednost koja se postavlja za sirinu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__sirina = value
    
    @property
    def visina(self):
        '''
         Getter za vracane vrednosti visine
        '''
        return self.__visina
    
    @visina.setter
    def visina(self, value):
        '''
        Setter za inicijalizovanje vrednosti visine
        
        :param value: vrednost koja se postavlja za visinu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__visina = value
        
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(super().__str__(), self.red, self.kolona, self.pozicija, self.duzina, self.sirina, self.visina, self.sekcija)

    
class Artikal(Identifikacija):
        
    def __init__(self, oznaka, naziv, opis, cena, rok_trajanja, polica):
            
        super().__init__(oznaka=oznaka)
        self.naziv = naziv
        self.opis = opis
        self.cena = cena
        self.rok_trajanja = rok_trajanja
        self.polica = polica
        
    @property
    def cena (self):
        '''
         Getter za vracane vrednosti cene
        '''      
        return self.__cena
        
    @cena.setter
    def cena (self, value):

        '''
        Setter za inicijalizovanje vrednosti cene
    
        :param value: vrednost koja se postavlja za cenu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__cena = value
            
    def __str__(self):
        '''
        Metoda koja vraca tekstualnu prezentaciju za Artikal
        '''
        return"{} {} {} {} {} {}".format(super().__str__(), self.naziv, self.opis, self.cena, self.rok_trajanja, self.polica)

        
class Stavka(Identifikacija):
            
    def __init__(self, oznaka, kolicina, ukupna_cena, artikal, racun):
            
        super().__init__(oznaka=oznaka)
        self.kolicina = kolicina
        self.ukupna_cena = ukupna_cena
        self.artikal = artikal
        self.racun = racun
            
    @property
    def kolicina (self):
        '''
         Getter za vracane vrednosti kolicine
        '''      
        return self.__kolicina
        
    @kolicina.setter
    def kolicina (self, value):

        '''
        Setter za inicijalizovanje vrednosti kolicine
        
        :param value: vrednost koja se postavlja za kolicinu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__kolicina = value
        
    @property
    def ukupna_cena (self):
        '''
         Getter za vracane vrednosti ukupne cene
        '''      
        return self.__ukupna_cena
        
    @ukupna_cena.setter
    def ukupna_cena (self, value):

        '''
        Setter za inicijalizovanje vrednosti ukupne cene
        
        :param value: vrednost koja se postavlja za ukupnu cenu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__ukupna_cena = value
        
    def __str__(self):
        return "{} {} {} {} {}".format(super().__str__(), self.kolicina, self.ukupna_cena, self.artikal, self.racun)

    
class Racun(Identifikacija):
        
    def __init__(self, oznaka, prodavac, ukupna_cena, datum):
            
        super().__init__(oznaka)
        self.prodavac = prodavac
        self.ukupna_cena = ukupna_cena
        self.datum = datum
            
    @property
    def ukupna_cena (self):
        '''
         Getter za vracane vrednosti ukupne cene
        '''      
        return self.__ukupna_cena
        
    @ukupna_cena.setter
    def ukupna_cena (self, value):

        '''
        Setter za inicijalizovanje vrednosti ukupne cene
        
        :param value: vrednost koja se postavlja za ukupnu cenu
        '''
        if value <= 0:
            raise ValueError("Vrednost mora biti veca od nule!")
        self.__ukupna_cena = value  

    def __str__(self):
        '''
        Metoda koja vraca tekstualnu prezentaciju za Racun
        '''
        return"{} {} {} {} ".format(super().__str__(), self.prodavac, self.ukupna_cena, self.datum)
            
