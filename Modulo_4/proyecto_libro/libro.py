# Definimos la clase Libro
class Libro:
    # Método constructor: se llama automáticamente al crear una instancia
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo             # Guarda el título del libro
        self.autor = autor               # Guarda el autor del libro
        self.paginas = paginas           # Guarda el total de páginas del libro
        self.paginas_leidas = 0          # Inicializamos las páginas leídas en 0

    # Método para mostrar toda la información del libro
    def mostrar_info(self):
        print(f"Título: {self.titulo}")                # Muestra el título
        print(f"Autor: {self.autor}")                  # Muestra el autor
        print(f"Páginas totales: {self.paginas}")      # Muestra la cantidad de páginas
        print(f"Páginas leídas: {self.paginas_leidas}")# Muestra el progreso de lectura

    # Método para simular la lectura de páginas
    def leer(self, paginas):
        self.paginas_leidas += paginas                 # Suma páginas leídas
        if self.paginas_leidas > self.paginas:         # No se puede leer más de lo que hay
            self.paginas_leidas = self.paginas
        return self                                     # Devuelve el objeto para encadenamiento

    # Método para mostrar el porcentaje de avance
    def progreso(self):
        porcentaje = (self.paginas_leidas / self.paginas) * 100   # Calcula el porcentaje
        print(f"Llevas leído un {porcentaje:.2f}% del libro.")    # Muestra con 2 decimales
        return self

    # Método de clase que permite crear un libro desde un string
    @classmethod
    def cargar_desde_string(cls, cadena):
        # La cadena debe estar en formato "título,autor,paginas"
        partes = cadena.split(",")                    # Divide la cadena en partes
        titulo = partes[0].strip()                    # Elimina espacios innecesarios
        autor = partes[1].strip()
        paginas = int(partes[2])
        return cls(titulo, autor, paginas)            # Retorna una nueva instancia de Libro

    # Método estático que verifica si un libro tiene más de 300 páginas
    @staticmethod
    def es_libro_grande(paginas):
        return paginas > 300                          # Retorna True o False
