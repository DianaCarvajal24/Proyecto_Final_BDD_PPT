import random


def jugar ():
    usuario = input("Escoja una opción:  'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n").lower()
    computadora = random.choice (['pi','pa','ti']);         

    if usuario == computadora:  
        print('usuario: '+usuario)   
        print('computadora: '+computadora)    
        return '¡Empate!'   

    if gano_el_jugador(usuario,computadora): 
        print('usuario: '+usuario)   
        print('computadora: '+computadora)    
        return '¡Ganaste!'

    print('usuario: '+usuario)   
    print('computadora: '+computadora)
    return '¡Perdiste!'


def gano_el_jugador (jugador,oponente):
    #Retornar el valor TRUE si gaba el jugador
    # Si el jugador saca:
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana Papel (ti > pa).
    # Papel gana Piedra (pa > pi).

    if ((jugador == 'pi' and oponente == 'ti') 
    or (jugador == 'ti' and oponente == 'pa')
    or (jugador == 'pa' and oponente == 'pi')):

        return True

    else: 
        return False

print(jugar())


    

