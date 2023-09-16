#Kalkulator do podstawowych obliczen z wykorzystaniem pętli while true
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

while True:

    a = float(input('Wprowadz 1 liczbe: '))

    b = float(input('Wprowadz 2 liczbe: ')) 

    #Liczby są zrobione przy użyciu float, żeby móc robić obliczenia z liczbami po przecinku
    
    znak = input('Podaj znak działania jakiego bedziesz wykonywac : ')

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
    
    #Możliwość ponownego policzenia bez ponownego uruchomienia
    while True:
        once_again = input('Czy chcesz ponownie obliczyć jakąś liczbe? (y/n): ')
        if once_again.lower() == 'y':
            break #Ponownie załaduje kalkulator
        elif once_again.lower() == 'n':
            exit() #zakonczenie programu
        else:
            print('Nie prawidłowy znak.')
