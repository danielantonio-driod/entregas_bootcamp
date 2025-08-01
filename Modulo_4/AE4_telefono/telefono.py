class Telefono:
    def __init__(self, marca, modelo, tipo):
        # Inicializamos atributos básicos
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        # Creamos una lista para guardar el historial de llamadas
        self.historial = []

    def llamar(self, numero):
        """
        Simula una llamada al número dado:
        1. Añade el número al historial.
        2. Imprime por pantalla la acción de llamar.
        """
        # Guardamos el número en el historial
        self.historial.append(numero)
        # Simulamos la llamada
        print(f"📞 Llamando al {numero} con {self.marca} {self.modelo} ({self.tipo})...")

    def ver_historial(self):
        """
        Muestra el listado de números a los que se ha llamado.
        """
        if not self.historial:
            print("No hay llamadas registradas.")
        else:
            print("Historial de llamadas:")
            for idx, num in enumerate(self.historial, start=1):
                print(f"  {idx}. {num}")

# Ejemplo de uso
if __name__ == "__main__":
    mi_telefono = Telefono("Samsung", "Galaxy S21", "Smartphone")
    mi_telefono.llamar("+56912345678")
    mi_telefono.llamar("+56987654321")
    mi_telefono.ver_historial()
