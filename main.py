import random
banknoty = [500, 200, 100, 50, 20, 10, 5, 2, 1,0.50,0.20, 0.10, 0.05, 0.02, 0.01]
cena = random.randint(1,1000)
print('Czy posiadasz karte biedronki?')
ODP = input()
if ODP in ["TAK", "tak","Tak", "posiadam", " tak posiadam", "jasne","tak poproszę"]:
    cena -= cena * 0.1
    print('Rabat 10% został odjęty od rachunku')
    print('do zapłaty', cena, sep=' ')

pieniadzeklienta = round(float(input()),2)
money = pieniadzeklienta - cena
Change = []



def run(money):
    for obj in banknoty:
        if money >= obj:
            money -= obj
            Change.append(obj)
            run(money)
            return


run(money)
print('to twoja reszta', Change, 'ZŁ', sep=' ')
