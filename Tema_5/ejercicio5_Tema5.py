def bisiesto():

    anho= int(input("Introduce el año para comprobar: "))
    anhoBisiesto=False

    while anhoBisiesto == False:

        if anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0):
            anhoBisiesto = True
            print(f"\nEl año {anho} es BISIESTO")
        else:
            print(f"\nNO es bisiesto el año {anho}\n")
            anho= int(input("Introduce otro año: "))

bisiesto()