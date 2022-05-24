a = 10
b = 20
c = 30

# indentazione è parte integrante della sintassi di python

if a > b:
    print('a è maggiore di b')
elif a == b:
    print('a è uguale a b')
else:
    print('a è minore di b')
    
# cicli
i = 1
while i < 10:
    print(f'il valore di i è {i}')
    i = i + 1

print('quasi', end=' ') # serve per non andare a capo dopo il print
print('finito') # di default end = '\n' il carattere che manda a capo
print('finito')