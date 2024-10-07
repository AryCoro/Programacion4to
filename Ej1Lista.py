##Turnos de videojuego
import random

vida_A = 100
vida_B = 100
ataque_A = 20
ataque_B = 15


turno = random.choice(['A', 'B'])

while vida_A > 0 and vida_B > 0:
    if turno == 'A':
        vida_B -= ataque_A
        print (f"A ataca. Vida de B: {vida_B}")
        turno = 'B'
else:
    vida_A -=ataque_B
    print (f"B ataca. Vida de A:{vida_A}")
    turno= 'A'

if vida_A <= 0:
    print("B gana.")
else:
    print("A gana.")
