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

# --- ACTUALIZAR VALORES ---

def actualizarDatos():
    matriz[1][0] = 6
    cantantes[0]["nombre"] = "Enrique Martin Morales"
    ciudades["México"][2] = "Monterrey"
    coordenadas[0]["latitud"] = 9.9355431
    print("\n✅ Datos actualizados correctamente.\n")

# --- FUNCIONES PARA MOSTRAR DATOS ---

def mostrarCantantes(cantantes):
    print("\n--- Lista de Cantantes ---")
    for c in cantantes:
        print(f"nombre - {c['nombre']}, pais - {c['pais']}")

def mostrarValoresClave(clave, cantantes):
    print(f"\n--- Valores de la clave '{clave}' ---")
    for c in cantantes:
        print(c.get(clave, "Clave no encontrada"))

def mostrarCostaRicaInfo(diccionario):
    print("\n--- Información de Costa Rica ---")
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()

# --- MENÚ INTERACTIVO ---

def menu():
    while True:
        print("\n📋 MENÚ DE FUNCIONES")
        print("1. Actualizar valores de las estructuras")
        print("2. Mostrar nombre y país de cada cantante")
        print("3. Mostrar solo los nombres de cantantes")
        print("4. Mostrar solo los países de cantantes")
        print("5. Mostrar información detallada de Costa Rica")
        print("6. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            actualizarDatos()
        elif opcion == "2":
            mostrarCantantes(cantantes)
        elif opcion == "3":
            mostrarValoresClave("nombre", cantantes)
        elif opcion == "4":
            mostrarValoresClave("pais", cantantes)
        elif opcion == "5":
            mostrarCostaRicaInfo(costa_rica)
        elif opcion == "6":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# --- EJECUCIÓN ---

if __name__ == "__main__":
    menu()
