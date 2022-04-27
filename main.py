import random

banknoty = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
cena = random.randint(1, 1000)
def karta(cena):
    print('Czy posiadasz karte biedronki?')
    ODP = input()
    if ODP in ["TAK", "tak", "Tak", "posiadam", " tak posiadam", "jasne", "tak poproszę", "jest", "mam","dysponuje", "dysponuję","tak mam","no",]:
        cena -= cena * 0.1
        print('Rabat 10% został odjęty od rachunku')
        print('do zapłaty', cena, 'zł', sep=' ')
        return cena
    elif ODP in ["nie","Nie","NIE"]:
        print('zachęcamy do założenia')
        print('do zapłaty', cena, 'zł', sep=' ')
        return cena
    elif ODP in ["sekunda","sekunda sprawdze","SEKUNDA","ZARAZ SPRAWDZE","zaraz sprawdzę"]:
        return karta(cena)

cena = karta(cena)

pieniadzeklienta = round(float(input()), 2)
money = pieniadzeklienta - cena
Change = []


def run(money):
    for obj in banknoty:
        if money >= obj:
            money -= obj
            print(money)
            Change.append(obj)
            run(money)
            return


run(money)
print("Oto pańska reszta", Change, "ZŁ", "Zapraszamy Ponownie", sep=' ')

