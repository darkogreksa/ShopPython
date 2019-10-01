'''
Created on 21.06.2019.

@author: Greksa
'''
from aplikacija.meniji import sekcije_izbor, glavni_meni, police_izbor,\
    artikli_izbor, stavke_izbor, racuni_izbor

'''
Glavni meni iz kojeg se pokrece aplikacija
'''


if __name__ == '__main__':
    try:
        print()
        print("Aplikacija za vodjenje evidencije artikala i racuna za prodavnice")
        print("================================================================")
        print()
        opcija="0"
        while opcija !="X":
            opcija = glavni_meni()
            if opcija=="1":
                print()
                sekcije_izbor()
            if opcija=="2":
                print() 
                police_izbor()
            if opcija =="3":
                print()
                artikli_izbor()
            if opcija =="4":
                print()
                stavke_izbor()
            if opcija =="5":
                print()
                racuni_izbor()
        print("Dovidjenja")
    except Exception as e:
        print(e)