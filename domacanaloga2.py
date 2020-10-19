print('Welcome to km/miles converter')

# Prva domača naloga
ponovitev = 'yes'
while True:
    if ponovitev == 'yes' or ponovitev == 'yeah':
        stevilo_km = float(input('Input the number of kilometres you want to convert: '))
        milje = 0.62*stevilo_km
        print('To je: ', milje)
        ponovitev = input('Would you like to convert any other number?')
        ponovitev = ponovitev.lower()
    else:
        print('Thank you, see you next time!')
        break


# Domača naloga 2.2: FizzBuzz

x=1
#fizz deljivo s 3
#buzz deljivo s 5
stevilo = int(input('Vnesi število med 1 in 100:'))
while x <= stevilo:
    if x % 5 == 0 and x % 3 == 0:
        print ('fizz_buzz')
    elif x % 3 == 0:
        print ('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print (x)
    x= x + 1