from tamagochi.tamagochi import Tamagochi
from persona.persona import Persona

mi_tamagochi = Tamagochi("Gozarutchi", "verde")
yo = Persona("Daniel", "Arrieta", mi_tamagochi)

#yo.darle_comida()
#yo.curarlo()
#yo.jugar_con_tamagochi()
#yo.dormir()
yo.estado() #debe dejarse una sola opción al momento de ejecutar

print(f"Nombre: {mi_tamagochi.nombre}")
print(f"Color: {mi_tamagochi.color}")
print(f"Salud: {mi_tamagochi.salud}")
print(f"Felicidad: {mi_tamagochi.felicidad}")
print(f"Energía: {mi_tamagochi.energia}")
