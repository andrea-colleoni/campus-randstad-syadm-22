numeri_1 = [1, 5, 10, 21, 9, 14, 11, 20, 40, -4]
numeri_2 = [12, 54, 9, 10, 17, 22, 97, 19, 66, -18, -9]

somma = 0
max = -1000000

for n in numeri_1:
    somma += n
    if n > max:
        max = n

print(f'1. la somma dei numeri è {somma}')
print(f'2. la media dei numeri è {somma / len(numeri_1)}')
print(f'3. il valore massimo è {max}')

# ripeto il ciclo solo per andare in ordine con la consegna
for n in numeri_1:
    if n % 2 == 0:
        print(f'Numero pari: {n}')

for n in numeri_1:
    for m in numeri_2:
        if n == m:
            print(f'5. {n} è un numero in comune tra le due liste')
            break

for n in numeri_2:
    trovato = False
    for m in numeri_1:
        if n == m:
            trovato = True
            break
    if not trovato:
        print(f'6. Il numero {n} non è presente nella prima lista')

tutti = numeri_1 + numeri_2
# bubble sort
i = 0
while i < len(tutti) - 1:
    j = i + 1
    while j < len(tutti):
        if tutti[j] < tutti[i]:
            appoggio = tutti[j] 
            tutti[j] = tutti[i]
            tutti[i] = appoggio
        j += 1
    i += 1

print(tutti)