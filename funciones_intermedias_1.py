#PARTE_1

# Datos
matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]

#cambios
matriz[1][0] = 6 #reemplaza de la segunda fila el primer item (considerando que inicia desde 0)
cantantes[0]["nombre"] = "Enrique Martin Morales" #reemplaza de la prinera fila el Nombre)
ciudades["México"][2] = "Monterrey" #reemplaza el tercer item del diccionario "Mexico"
coordenadas[0]["latitud"] = 9.9355431 #reemplaza latitud, es 0 porque hay un único item

#print_resultados
print("Matriz actualizada:")
print(matriz)

print("\nCantantes actualizados:")
print(cantantes)

print("\nCiudades actualizadas:")
print(ciudades)

print("\nCoordenadas actualizadas:")
print(coordenadas)


#PARTE_2 y PARTE_3

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#funcion
#for diccionario in lista: Recorre cada diccionario de la lista (uno por uno).
#for clave, valor in diccionario.items(): Recorre las parejas clave/valor del diccionario actual.
#print(f"{clave} - {valor}") Imprime la información en el formato pedido.


def iterarDiccionario(lista):
    for diccionario in lista:
        for clave, valor in diccionario.items():
            print(f"{clave} - {valor}")

iterarDiccionario(cantantes)

#PARTE_3
#funcion
# for diccionario in lista: → Recorremos cada diccionario.
#if llave in diccionario: → Nos aseguramos de que la clave exista para evitar errores.
#print(diccionario[llave]) → Mostramos el valor asociado a esa clave.

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

iterarDiccionario2("nombre", cantantes)

iterarDiccionario2("pais", cantantes)

#PARTE_4

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#funcion
#for clave, lista in diccionario.items(): Recorre cada par clave/lista del diccionario.

#len(lista) Nos da el número de elementos en la lista.

#clave.upper() Convierte la clave a mayúsculas como pide el enunciado.

#Segundo for: Recorre cada elemento dentro de la lista y lo imprime.

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()  # línea en blanco para separar secciones

imprimirInformacion(costa_rica)
