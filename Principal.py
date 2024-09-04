from Perinola import Perinola1
from Apuesta import Apuesta
from Jugador import Jugador
p = Perinola1()

tiras= p.tirar()

print(p)



a = Apuesta()

a.ponerFichas(5)

print(a)



jugador = Jugador("BenjaMartinez", 15)

print(jugador) 