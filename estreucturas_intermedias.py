# --- DATOS BASE ---

matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# --- ACTUALIZACIÓN DE DATOS ---

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("\n DATOS ACTUALIZADOS\n")
print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)

# --- PARTE 2: RECORRER LISTA DE DICCIONARIOS ---

print("\n INFORMACIÓN DE CANTANTES (nombre y país)")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

# --- PARTE 3: OBTENER VALORES POR CLAVE ---

print("\n SOLO NOMBRES DE CANTANTES:")
for cantante in cantantes:
    print(cantante["nombre"])

print("\n SOLO PAÍSES DE CANTANTES:")
for cantante in cantantes:
    print(cantante["pais"])

# --- PARTE 4: RECORRER DICCIONARIO CON LISTAS ---

print("\n INFORMACIÓN DETALLADA DE COSTA RICA")
for clave, lista in costa_rica.items():
    print(f"{len(lista)} {clave.upper()}")
    for item in lista:
        print(item)
    print()  # Línea en blanco para separar
