banknoty = [500,200,100,50,20,10,5,2,1]
money = int(input())
print('Czy posiadasz karte biedronki?')
if input()=="TAK":
    money -= money * 0.1
    print('Rabat 10% został odjęty od rachunku')
    print('do zapłaty', money, sep=' ')

Change = []

def run(money):
    for obj in banknoty:
        if money >= obj:
            money -= obj
            Change.append(obj)
            run(money)
            return
run(money)
print('to twoja reszta', Change, 'ZŁ' , sep=' ')
