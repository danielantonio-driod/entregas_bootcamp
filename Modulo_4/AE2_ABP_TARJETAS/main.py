from tarjetas import TarjetaCredito

# Lista para guardar referencias a las tarjetas creadas
tarjetas = []

def crear_tarjeta():
    try:
        limite = float(input("Ingrese el límite de crédito: "))
        interes = float(input("Ingrese el interés (por ejemplo 0.02 para 2%): "))
        tarjeta = TarjetaCredito(limite_credito=limite, intereses=interes)
        tarjetas.append(tarjeta)
        print("✅ Tarjeta creada correctamente.\n")
    except ValueError:
        print("❌ Error: Ingrese valores numéricos válidos.\n")

def realizar_compra():
    if not tarjetas:
        print("⚠️ No hay tarjetas disponibles.\n")
        return
    mostrar_tarjetas()
    try:
        index = int(input("Seleccione el número de tarjeta: ")) - 1
        monto = float(input("Ingrese el monto de la compra: "))
        tarjetas[index].compra(monto)
    except (IndexError, ValueError):
        print("❌ Selección inválida.\n")

def realizar_pago():
    if not tarjetas:
        print("⚠️ No hay tarjetas disponibles.\n")
        return
    mostrar_tarjetas()
    try:
        index = int(input("Seleccione el número de tarjeta: ")) - 1
        monto = float(input("Ingrese el monto del pago: "))
        tarjetas[index].pago(monto)
    except (IndexError, ValueError):
        print("❌ Selección inválida.\n")

def cobrar_intereses():
    if not tarjetas:
        print("⚠️ No hay tarjetas disponibles.\n")
        return
    mostrar_tarjetas()
    try:
        index = int(input("Seleccione el número de tarjeta: ")) - 1
        tarjetas[index].cobrar_interes()
        print("✅ Intereses aplicados.\n")
    except (IndexError, ValueError):
        print("❌ Selección inválida.\n")

def mostrar_tarjetas():
    if not tarjetas:
        print("⚠️ Aún no se han creado tarjetas.\n")
        return
    print("📋 Lista de tarjetas:")
    for i, tarjeta in enumerate(tarjetas, 1):
        print(f"{i}. Saldo: ${tarjeta.saldo_pagar:.2f} | Límite: ${tarjeta.limite_credito:.2f} | Interés: {tarjeta.intereses*100:.2f}%")
    print()

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Crear nueva tarjeta")
    print("2. Realizar compra")
    print("3. Realizar pago")
    print("4. Cobrar intereses")
    print("5. Mostrar tarjetas")
    print("6. Mostrar resumen general (BONUS)")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_tarjeta()
        elif opcion == "2":
            realizar_compra()
        elif opcion == "3":
            realizar_pago()
        elif opcion == "4":
            cobrar_intereses()
        elif opcion == "5":
            mostrar_tarjetas()
        elif opcion == "6":
            TarjetaCredito.mostrar_todas_las_tarjetas()
        elif opcion == "0":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
