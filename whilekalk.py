#Kalkulator do podstawowych obliczen z wykorzystaniem pętli while true
#Zaciagniecie biblioteki matematycznej żeby była możliwosc pierwiastkowania.
import math 

print('******** Witaj na swoim Pythonowym Kalkulatorze ********')
print(' ')
print(' ')
print('        Dozwolone znaki        ')
print(' ')
print('*******************************')
print('* Dodawanie to " + "          *')
print('* Odejmowanie to " - "        *')
print('* Mnożenie to " * "           *')
print('* Dzielenie to " / "          *')
print('* Potegowanie to " ** "       *')
print('* Pierwiastkowanie to "sqrt"  *')
print('*******************************')
print(' ')
print('**** Zaczynamy ****')
print(' ')

while True:
   
    znak = input('Podaj znak działania jakiego bedziesz wykonywac : ')

    #Liczby są zrobione przy użyciu float, żeby móc robić obliczenia z liczbami po przecinku. Jeśli nie ma takiej potrzeby można użyć int zamiast float.

    #Dodawanie
    if znak == '+':
        a = float(input('Wprowadz 1 liczbe: '))
        b = float(input('Wprowadz 2 liczbe: '))
        print(a + b)
    #Odejmowanie
    elif znak == '-':
        a = float(input('Wprowadz 1 liczbe: '))
        b = float(input('Wprowadz 2 liczbe: '))
        print(a - b)
    #Mnożenie
    elif znak == '*':
        a = float(input('Wprowadz 1 liczbe: '))
        b = float(input('Wprowadz 2 liczbe: '))
        print(a * b)
    #Dzielenie
    elif znak == '/':
        a = float(input('Wprowadz 1 liczbe: '))
        b = float(input('Wprowadz 2 liczbe: '))
        if b != 0:
            print(a/b)
        else:    
            print("Nie można dzielić przez zero.")
    #Potęgowanie
    elif znak == '**':
        a = float(input('Wprowadz 1 liczbe: '))
        b = float(input('Wprowadz 2 liczbe: '))
        print(a ** b)
    #Pierwiastkowanie
    elif znak == 'sqrt':
        c = float(input('Wprowadz liczbe: '))
        if c >= 0:
            print(math.sqrt(c))
        else:
            print('Nie można obliczyć pierwiastka z liczby ujemnej.')
    #Błedny znak
    else:
        print("Podałeś zły znak!")
    
    #Możliwość ponownego policzenia bez ponownego uruchomienia
    while True:
        once_again = input('Czy chcesz ponownie obliczyć jakąś liczbe? (yes/no): ')
        if once_again.lower() == 'y' or 'yes':
            break #Ponownie załaduje kalkulator
        elif once_again.lower() == 'n' or 'no':
            exit() #zakonczenie programu
        else:
            print('Nie prawidłowy znak.')
