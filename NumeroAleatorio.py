# =============================================================================
# Hay que crear un juego en el cual el usuario debe adivinar un número.
# 
# El programa debe generar un número aleatorio entre 1 y 10. A continuación se le pedirá al usuario que escriba un número.
# A continuación se le dirá al usuario si ha acertado el número o si ha fallado.
# 
# Si ha acertado, el programa finalizará.
# 
# En esta primera versión del programa, si ha fallado, se le volverá a pedir al usuario otro número hasta que acierte.
#
# Autor: Oscar Albarracin
# 
# Fecha: 28-10-2021
# =============================================================================

min = 1
max = 10


def numeroAleatorio(min, max):
    ''' Devuelve un valor aleatorio entre min y max, inclusives'''
    import random
    return random.randrange(min, max + 1)


def dime_numero():
    '''Devuelve el numero introducido'''
    numero = int(input("Dime un numero entre el 1 y el 10: "))
    return numero


numero_generado = numeroAleatorio(min, max)

while True:
    d_numero = dime_numero()
    if d_numero != numero_generado:
        print("Lo siento no has acertado sigue intentandolo")
    else:
        print("Felicidades lo as acertado")
        break
