class TarjetaCredito:
    # Lista para guardar todas las instancias creadas
    tarjetas_creadas = []

    # Constructor con valor por defecto para saldo_pagar
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar  # Monto inicial a pagar
        self.limite_credito = limite_credito  # Límite de la tarjeta
        self.intereses = intereses  # Interés en decimal (ej: 0.02)
        TarjetaCredito.tarjetas_creadas.append(self)  # Guarda la instancia

    # Método para realizar una compra
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self  # Permite encadenar métodos

    # Método para pagar el saldo
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  # Permite encadenar métodos

    # Método para mostrar información de la tarjeta
    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self  # Permite encadenar métodos

    # Método para cobrar interés
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  # Permite encadenar métodos

    # Método de clase para mostrar todas las tarjetas
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("Resumen de todas las tarjetas:")
        for i, tarjeta in enumerate(cls.tarjetas_creadas, 1):
            print(f"Tarjeta {i}: Saldo=${tarjeta.saldo_pagar:.2f}, Límite=${tarjeta.limite_credito}, Interés={tarjeta.intereses*100:.2f}%")
