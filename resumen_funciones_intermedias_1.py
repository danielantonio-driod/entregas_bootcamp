# Datos base
cantantes = [
    {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Funciones
def iterarDiccionario(lista):
    for dic in lista:
        for clave, valor in dic.items():
            print(f"{clave} - {valor}")

def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()

# Menú principal
def menu():
    while True:
        print("\n📋 MENÚ DE FUNCIONES")
        print("1. Mostrar todos los datos de cantantes")
        print("2. Mostrar solo nombres de cantantes")
        print("3. Mostrar solo países de cantantes")
        print("4. Mostrar información detallada de Costa Rica")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            iterarDiccionario(cantantes)
        elif opcion == "2":
            iterarDiccionario2("nombre", cantantes)
        elif opcion == "3":
            iterarDiccionario2("pais", cantantes)
        elif opcion == "4":
            imprimirInformacion(costa_rica)
        elif opcion == "5":
            print("👋 Hasta luego, Daniel5.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar
menu()
