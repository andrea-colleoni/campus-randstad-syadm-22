#Andrea Frigerio 19/05/2022
import os
a=1
b=1
def triangolo(n):   #triangolo
    print("\nTriangolo")
    e=0
    while e<n:
        e+=1
        j=e;
        while(j>0):
            print('*', end = ' ')
            j-=1
        print()
def triangoloReverse(n):    #triangolo al contrario
    print("\nTriangolo al contrario")
    e=0
    while e<n:
        j=n-e;
        e+=1
        while(j>0):
            print('*', end = ' ')
            j-=1
        print()
def quadrato(n):    #quadrato nxn
    print("\nQuadrato")
    e=0
    while e<n:
        e+=1
        j=0;
        while j<n:
            print('*', end = ' ')
            j+=1
        print()
def quadratoVuoto(n):   #quadrato nxn vuoto
    print("\nQuadrato vuoto")
    e=0
    while e<n:
        e+=1
        j=0;
        while j<int(var):
            if (e >= 2 and e <= n-1) and (j >= 1 and j <= n-2):
                print(' ', end = ' ')
            else:
                print('*', end = ' ')
            j+=1
        print()
def reset():
    input("Premi INVIO.")
    os.system('cls')
print("Programma di Andrea Frigerio")
while b!=0:     #main function
    while a!=0:
        var=input("Inserisci valore numerico intero e maggiore di 0: ")
        if var.isnumeric() and int(var)>0:
            a=0
        else:
            if var=="exit":
                a=0
                b=0
            else:
                print("Non è un numero intero, maggiore di 0.")
                reset()
    if b!=0:
        triangolo(int(var))
        triangoloReverse(int(var))
        quadrato(int(var))
        quadratoVuoto(int(var))
        reset()
        a=1