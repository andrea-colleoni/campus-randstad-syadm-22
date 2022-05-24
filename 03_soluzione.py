tipoFigura = 'd'
righeFigura = 5
simboloDaStampare = '*'

iterazioneRiga = 1

if tipoFigura == 'a':
    while iterazioneRiga <= righeFigura:
        iterazioneColonna = 1
        while iterazioneColonna <= iterazioneRiga:
            print(simboloDaStampare, end = '')
            iterazioneColonna += 1
        print()
        iterazioneRiga += 1
    print()
    print('triangolo')
elif tipoFigura == 'b':
    while iterazioneRiga <= righeFigura:
        iterazioneColonna = (righeFigura - iterazioneRiga)
        while iterazioneColonna > 0:
            print(simboloDaStampare, end = '')
            iterazioneColonna -= 1
        print()
        iterazioneRiga += 1
    print()    
    print('triangolo rovesciato')
elif tipoFigura == 'c':
    while iterazioneRiga <= righeFigura:
        iterazioneColonna = righeFigura
        while iterazioneColonna > 0:
            print(simboloDaStampare, end = '')
            iterazioneColonna -= 1
        print()
        iterazioneRiga += 1    
    print('quadrato pieno')
elif tipoFigura == 'd':
    while iterazioneRiga <= righeFigura:
        iterazioneColonna = righeFigura
        while iterazioneColonna > 0:
            if iterazioneRiga == 1 or iterazioneRiga == righeFigura or iterazioneColonna == 1 or iterazioneColonna == righeFigura:
                print(simboloDaStampare, end = '')
            else:
                print(' ', end = '')
            iterazioneColonna -= 1
        print()
        iterazioneRiga += 1        
    print('quadrato vuoto')
else:
    print('scelta non valida')