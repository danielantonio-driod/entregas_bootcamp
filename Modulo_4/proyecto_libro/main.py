from libro import Libro  # Importamos la clase Libro

# Lista para guardar todos los libros disponibles en memoria
biblioteca = []

# Instanciamos tres libros relacionados a tus proyectos/persona
libro1 = Libro("DAV-DEV: Manual del Creador Fullstack", "Daniel Arrieta Vega", 320)
libro2 = Libro("D-Labs: Secretos de un Taller Legendario", "Daniel Arrieta Vega", 280)
libro3 = Libro("Más Fuerte que el TDAH: Código, Café y Bicicletas", "Daniel Arrieta Vega", 360)

# Cargamos las instancias a la lista biblioteca
biblioteca.extend([libro1, libro2, libro3])

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n📚 Menú de Biblioteca")
    print("1. Crear libro manualmente")
    print("2. Crear libro desde cadena (formato: título,autor,páginas)")
    print("3. Leer páginas de un libro")
    print("4. Ver progreso de un libro")
    print("5. Mostrar info de todos los libros")
    print("6. Verificar si un libro es grande")
    print("0. Salir")

# Función para permitir al usuario seleccionar un libro de la lista
def seleccionar_libro():
    if not biblioteca:
        print("❌ No hay libros en la biblioteca.")
        return None
    for i, libro in enumerate(biblioteca):
        print(f"{i + 1}. {libro.titulo} ({libro.autor})")  # Muestra libros con número
    try:
        index = int(input("Selecciona el número del libro: ")) - 1
        if 0 <= index < len(biblioteca):
            return biblioteca[index]   # Retorna el libro seleccionado
        else:
            print("❌ Opción inválida.")
            return None
    except ValueError:
        print("❌ Entrada no válida.")
        return None

# Bucle principal que se repite hasta que el usuario elija salir
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Crear libro manualmente
        titulo = input("Título: ")
        autor = input("Autor: ")
        try:
            paginas = int(input("Páginas: "))
            libro = Libro(titulo, autor, paginas)
            biblioteca.append(libro)
            print("✅ Libro agregado correctamente.")
        except ValueError:
            print("❌ Error: las páginas deben ser un número.")

    elif opcion == "2":
        # Crear libro desde un string (ejemplo: "Libro X,Autor Y,123")
        cadena = input("Ingresa la cadena: ")
        try:
            libro = Libro.cargar_desde_string(cadena)
            biblioteca.append(libro)
            print("✅ Libro creado desde cadena.")
        except Exception as e:
            print(f"❌ Error al crear libro: {e}")

    elif opcion == "3":
        # Leer páginas de un libro
        libro = seleccionar_libro()
        if libro:
            try:
                paginas = int(input("¿Cuántas páginas deseas leer? "))
                libro.leer(paginas)
                print("📖 Lectura registrada.")
            except ValueError:
                print("❌ Entrada inválida.")

    elif opcion == "4":
        # Ver porcentaje de progreso
        libro = seleccionar_libro()
        if libro:
            libro.progreso()

    elif opcion == "5":
        # Mostrar todos los libros disponibles
        if not biblioteca:
            print("📂 No hay libros cargados.")
        for libro in biblioteca:
            libro.mostrar_info()
            print("-" * 40)

    elif opcion == "6":
        # Ver si un libro es considerado grande
        libro = seleccionar_libro()
        if libro:
            if Libro.es_libro_grande(libro.paginas):
                print("📏 Es un libro grande.")
            else:
                print("📏 No es un libro grande.")

    elif opcion == "0":
        # Salida del programa
        print("👋 Hasta luego.")
        break

    else:
        print("❌ Opción inválida.")
