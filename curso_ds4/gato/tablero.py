'''
tablero.py: Dibuja el tablero de juego del gato
'''
import random


def dibuja_tablero(simbolos_dict):
    '''dibuja el tablero del juego del gato'''
    print(f'''
    {simbolos_dict['1']} | {simbolos_dict['2']} | {simbolos_dict['3']}
    ---------
    {simbolos_dict['4']} | {simbolos_dict['5']} | {simbolos_dict['6']}
    ---------
    {simbolos_dict['7']} | {simbolos_dict['8']} | {simbolos_dict['9']}
    ''')
    def ia (simbolos:dict):
        '''Estrategia de la computadora'''
        ocupado= True
        while ocupado is True:
            x=random.choice(list(simbolos.keys()))
            if simbolos[x] not in ['X','O']:
                simbolos[x]='O'
                ocupado = False
    def usuario(simbolos:dict):
        '''estrategia de usuario'''
        ocupado=True
        lista_numeros=[str(i) for i in range(1,10)] #del 1 al 9
        while ocupado is True:
            x= input ('Elija un numero del 1 al 9')
            if x in lista_numeros:
                if simbolos[x] not in ['X','O']:
                    simbolos[x]='X'
                    ocupado=False

                else:
                    print('Esta casilla esta ocupada')
    def juego(simbolos:dict):
        '''juego del gato'''
        lista_combinaciones =[
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['1','4','7'],
            ['2','5','8'],
            ['3','6','9'],
            ['1','5','9'],
            ['3','5','7']
        ]
    def checa_winner(simbolos:dict,combianciones:list):
        '''Checa si hay un ganador'''
        for combinacion in combianciones:
            if simbolos[combinacion[0]] == simbolos[combinacion[1]] == simbolos[combinacion[2]]:
                return simbolos[combinacion[0]]
        return False
    if __name__ == '__main__':
        numeros = [str(i) for i in range(1,10)]
        dsimbolos = {x:x for x in numeros}
        dibuja_tablero(dsimbolos)
        usuario(dsimbolos)
        dibuja_tablero(dsimbolos)
        '''
        x = random.choice(numeros)
        numeros.remove(x)
        dsimbolos[x]= 'X'
        dibuja_tablero(dsimbolos)
        o = random.choice(numeros)
        numeros.remove(o)
        dsimbolos[o]= 'O'
        dibuja_tablero(dsimbolos)
        '''