# --- CLASE CLIENTE ---
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} ({self.correo})"


# --- CLASE MESA ---
class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.estado = "libre"

    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "libre"

    def __str__(self):
        return f"Mesa {self.numero} - Estado: {self.estado}"


# --- CLASE PEDIDO ---
class Pedido:
    def __init__(self, cliente, platos):
        self.cliente = cliente
        self.platos = platos
        self.total = self.calcular_total()
        self.estado = "pendiente"

    def calcular_total(self):
        precios = {"Sushi": 12000, "Tacos": 8000, "Pizza": 10000}
        return sum(precios.get(plato, 0) for plato in self.platos)

    def marcar_entregado(self):
        self.estado = "entregado"

    def __str__(self):
        return f"Pedido de {self.cliente.nombre}: {', '.join(self.platos)} - Total: ${self.total} - Estado: {self.estado}"


# --- CLASE RESERVA ---
class Reserva:
    def __init__(self, cliente, mesa):
        self.cliente = cliente
        self.mesa = mesa

    def realizar_reserva(self):
        if self.mesa.estado == "libre":
            self.mesa.ocupar()
            print(f"Reserva confirmada para {self.cliente.nombre} en la {self.mesa}")
        else:
            print(f"Error: {self.mesa} ya está ocupada")

    def cancelar(self):
        self.mesa.liberar()
        print(f"Reserva cancelada para {self.cliente.nombre}")


# --- CLASE RESTAURANTE ---
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = [Mesa(i) for i in range(1, 6)]
        self.pedidos = []

    def mostrar_mesas(self):
        for mesa in self.mesas:
            print(mesa)

    def buscar_mesa_libre(self):
        for mesa in self.mesas:
            if mesa.estado == "libre":
                return mesa
        return None

    def tomar_reserva(self, cliente):
        mesa_disponible = self.buscar_mesa_libre()
        if mesa_disponible:
            reserva = Reserva(cliente, mesa_disponible)
            reserva.realizar_reserva()
            return reserva
        else:
            print("No hay mesas disponibles")
            return None

    def tomar_pedido(self, cliente, platos):
        pedido = Pedido(cliente, platos)
        self.pedidos.append(pedido)
        print(f"Pedido tomado:\n{pedido}")
        return pedido

    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)


# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    restaurante = Restaurante("Sabores del Mundo")

    cliente1 = Cliente("Ana", "ana@mail.com")
    cliente2 = Cliente("Luis", "luis@mail.com")

    restaurante.mostrar_mesas()
    reserva1 = restaurante.tomar_reserva(cliente1)
    reserva2 = restaurante.tomar_reserva(cliente2)

    restaurante.mostrar_mesas()

    pedido1 = restaurante.tomar_pedido(cliente1, ["Sushi", "Tacos"])
    pedido1.marcar_entregado()

    restaurante.mostrar_pedidos()
