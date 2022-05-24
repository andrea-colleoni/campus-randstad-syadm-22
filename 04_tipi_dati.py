# dynamic types
str = 'ciao'
print(str)
str = 5
print(str)

colori = ['verde', 'giallo', 'blu', 'rosso'] # list
print(colori)
print(colori[1])
lista = [1, 'ciao', True, 4.6]
print(lista)

for c in colori:
    print(c)
colori.append('arancione')
for c in colori:
    print(c)
colori.insert(2, 'indaco')
print(colori)
colori.remove('blu')
print(colori) 
    
andrea = {
    "nome": "Andrea",
    "cognome": "Colleoni",
    "altezza": 183,
    "citta": "Bergamo"
} # dict
print(andrea['altezza'])
studenti = [
    { 
        "nome": "Mario",
        "cognome": "Rossi"
    },
    {
        "nome": "Anna",
        "cognome": "Verdi"
    }
]
for s in studenti:
    print(f"Lo studente {s['cognome']}, si chiama {s['nome']}")