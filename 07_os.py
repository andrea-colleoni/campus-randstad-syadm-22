import os

os.mkdir('esempi')
files = os.listdir()
for f in files:
    if f.endswith('.txt'):
        os.popen(f'copy {f} esempi') # impartisco comandi di sistema operativo
        os.popen(f'del {f}')