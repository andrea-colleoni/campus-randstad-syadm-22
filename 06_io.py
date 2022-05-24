# lo standard output è la tastiera
# per inviare bytes allo stdout uso print()
# print('bytes che vanno sulla console')

# lo standard input è la tastiera (keyboard)
# per ricevere bytes uso input()
# lettura = input('digita qualcosa: ')
# print(f'echo: {lettura}')

# file mode: r, w, a... rb, wb, ab,...
# r: read (è il default)
# w: write
# a: append
# il suffiso b, indica che il tipo di dato che leggo/scrivo/appendo è binario (se non metto b, sarà ASCII)
esempio = open('esempio.txt', 'r')
print(esempio.name)

testo = esempio.read(1)
print(f' è stato letto il seguente carattere: {testo}')
testo = esempio.read(1)
print(f' è stato letto il seguente carattere: {testo}')
testo = esempio.read(1)
print(f' è stato letto il seguente carattere: {testo}')
testo = esempio.read(1)
print(f' è stato letto il seguente carattere: {testo}')
testo = esempio.read(1)
print(f' è stato letto il seguente carattere: {testo}')

# liberare la risorsa (OS rimuove il lock)
esempio.close()

# lettura di un intero file
with open('esempio2.txt', 'r') as lettera:
    for riga in lettera:
        print(riga)

# scrittura (overwrite e contestuale creazione se il file non esiste) di un file di testo
risultato = open('risultato.txt', 'w')
risultato.write('Questo file è stato scritto da Python!')
risultato.close()

# trasferimento del contenuto da un file a un altro
copia = open('copia-lettera.txt', 'w')
with open('esempio2.txt', 'r') as lettera:
    copia.writelines(lettera)
copia.close()