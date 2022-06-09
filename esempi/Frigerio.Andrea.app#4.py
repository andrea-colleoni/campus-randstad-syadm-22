#Andrea Frigerio 25/05/2022
import os
import math

print("Programma di Andrea Frigerio")
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
def inputCheked(string):
    while True:
        var=input(string)
        if var.replace('.','',1).isdigit():
            return float(var)
        else:
            input("Non è un numero\nPremi INVIO.")
def areaQuadrato(lato):
    print(f'L\'area el quadrato è: {lato**2}') 
def areaRettangolo(base, altezza):
    print(base*altezza)
def areaTriangolo(base, altezza):
    print((base*altezza)/2)
def areaCerchio(raggio):
    print(math.pi*(raggio**2))
while True:
    os.system('cls')
    var=input("Inserisci il numero dell'opzione desiderata, altrimenti digitare \"exit\" per uscire\n1) Area Quadrato\n2) Area Rettangolo\n3) Area Triangolo\n4) Area Cerchio\n")
    if var.isnumeric() and int(var) in [1, 2, 3, 4]:
        match int(var):
            case 1:
                areaQuadrato(inputCheked("Inserisci il lato del quadrato: "))
            case 2:
                areaRettangolo(inputCheked("Inserisci la base del rettangolo: "), inputCheked("Inserisci l' altezza del rettangolo: "))
            case 3:
                areaTriangolo(inputCheked("Inserisci la base del triangolo: "), inputCheked("Inserisci l' altezza del triangolo: "))
            case 4:
                areaCerchio(inputCheked("Inserisci il raggio del cerchio: "))
    elif var=="exit":
        break
    else:
        print("Non è un opzione consentita.")
    input("Premi il punsante \"INVIO\"")