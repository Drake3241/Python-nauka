#Kalkulator do podstawowych obliczen z wykorzystaniem pętli while true

#Zaciagniecie biblioteki matematycznej żeby była możliwosc pierwiastkowania.
import math 

print('********Witaj na swoim Pythonowym Kalkulatorze********')
print(' ')
print('Dozwolone znaki: ')
print('Dodawanie to " + " ')
print('Odejmowanie to " - " ')
print('Mnożenie to " * " ')
print('Dzielenie to " / " ')
print('Potegowanie to " ** " ')
print('Pierwiastkowanie to "sqrt"')
print(' ')
print('****Zaczynamy****')
print(' ')

while True:
   
    znak = input('Podaj znak działania jakiego bedziesz wykonywac : ')

    if znak == 'sqrt':
        c = float(input('Wprowadz liczbe: ')) 
    else:
        a = float(input('Wprowadz 1 liczbe: '))

        b = float(input('Wprowadz 2 liczbe: ')) 

    #Liczby są zrobione przy użyciu float, żeby móc robić obliczenia z liczbami po przecinku. Jeśli nie ma takiej potrzeby można użyć int zamiast float.

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
        if b != 0:
            print(a/b)
        else:    
            print("Nie można dzielić przez zero.")
    #Potęgowanie
    elif znak == '**':
        print(a ** b)
    #Pierwiastkowanie
    elif znak == 'sqrt':
        if a >= 0:
            print(math.sqrt(a))
        else:
            print('Nie można obliczyć pierwiastka z liczby ujemnej.')
    #Błedny znak
    else:
        print("Podałeś zły znak!")
    
    #Możliwość ponownego policzenia bez ponownego uruchomienia
    while True:
        once_again = input('Czy chcesz ponownie obliczyć jakąś liczbe? (y/n): ')
        if once_again.lower() == 'y':
            break #Ponownie załaduje kalkulator
        elif once_again.lower() == 'n':
            exit() #zakonczenie programu
        else:
            print('Nie prawidłowy znak.')
