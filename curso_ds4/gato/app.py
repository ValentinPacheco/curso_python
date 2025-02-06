import tablero

def main():
    ''' Punto de entrada a la aplicacion '''
    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score = {"X":X,"O":O}
    numeros = {str(i):str(i) for i in range(1,10)}
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g)
        tablero.despliega_tablero(score)
    

if __name__ == '__main__':
    main()