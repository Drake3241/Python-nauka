#Kalkulator do podstawowych obliczen
print('********Witaj na swoim Pythonowym Kalkulatorze********')
print(' ')
print('Dozwolone znaki: ')
print('Dodawanie to " + " ')
print('Odejmowanie to " - " ')
print('Mnożenie to " * " ')
print('Dzielenie to " / " ')
print('Potegowanie to " ** " ')
print(' ')
print('****Zaczynamy****')
print(' ')

a = float(input('Wprowadz 1 liczbe: '))

znak = input('Podaj znak działania jakiego bedziesz wykonywac : ')

b = float(input('Wprowadz 2 liczbe: '))

#Dodawanie
if znak == '+':
    print(a + b)
#Odejmowanie
elif znak == '-':
    print(a - b)
#Mnożenie
elif znak == '*':
    print(a * b)
#Dzielenie
elif znak == '/':
    print(a / b)
#Potęgowanie
elif znak == '**':
    print(a ** b)
#Błedny znak
else:
    print("Podałeś zły znak!")
