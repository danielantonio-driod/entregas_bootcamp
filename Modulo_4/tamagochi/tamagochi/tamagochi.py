class Tamagochi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 50
        self.energia = 100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5

    def comer(self):
        self.felicidad += 5
        self.salud += 10

    def curar(self):
        self.salud += 20
        self.felicidad -= 5

    def dormir(self):
        self.energia += 20
        self.felicidad -= 5
        
    def estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.salud}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energía: {self.energia}")