class Persona:
    def __init__(self, nombre, apellido, mi_tamagochi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagochi = mi_tamagochi

    def jugar_con_tamagochi(self):
        self.tamagochi.jugar()

    def darle_comida(self):
        self.tamagochi.comer()

    def curarlo(self):
        self.tamagochi.curar()

    def dormir(self):
        self.tamagochi.dormir()

    def estado(self):
        self.tamagochi.estado
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        
    