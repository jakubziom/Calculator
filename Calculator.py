import math

while True:
    try:
        action = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:'))
        if action == 1 or action == 2 or action == 3 or action == 4:
            break
        else:
            print('Proszę podać cyfrę od 1 do 4')     
    except:
        print("Proszę podać cyfrę, nie tekst")
        continue

if action == 1 or action==3:
    while True:
        try:
            elements= int(input('Ile składników chcesz użyć?'))
            break
        except:
            print("Proszę podać liczbę całkowitą")

    elements_list=[]

    for i in range(0,elements):
        elements_list.append(0)

    for i in range(0,elements):
        try:
            elements_list[i] = float(input('Podaj składnik ' + str(i+1) +':'))
            continue
        except:
            print("Proszę podać liczbę, program uznał, że wpisałeś zero")


if action == 2 or action==4:
    while True:
        try:
            number1 = float(input('Podaj składnik 1:'))
            break
        except:
            print("Proszę podać liczbę")

    while True:
        try:
            number2 = float(input('Podaj składnik 2:'))
            break
        except:
            print("Proszę podać liczbę")


if action == 1:
    print('Dodaję:')
    print(*elements_list, sep=" + ")
    result = sum(elements_list)
    print('Wynik to '+str(result))
elif action == 2:
    print('Odejmuję:')
    print(str(number1) +' - '+ str(number2))
    result = number1-number2
    print('Wynik to '+str(result))
elif action == 3:
    print('Mnożę:')
    print(*elements_list, sep=" * ")  
    result = math.prod(elements_list)
    print('Wynik to '+ str(result))
elif action == 4:
    if number2==0:
        print('Nie można dzielić przez 0!')
        exit(0)
    print('Dzielę:')
    print(str(number1) +' : '+ str(number2))
    result = number1/number2
    print('Wynik to '+str(result))

