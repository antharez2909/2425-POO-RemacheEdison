# Clase que representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"


# Clase que representa una habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Hab. {self.numero} reservada.")
        else:
            print(f"Hab. {self.numero} ya está reservada.")

    def liberar(self):
        self.reservada = False
        print(f"Hab. {self.numero} liberada.")

    def __str__(self):
        return f"Hab. {self.numero} ({self.tipo}), Precio: {self.precio} USD"


# Clase que representa el sistema de reservas del hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)

    def realizar_reserva(self, cliente, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if not habitacion.reservada:
                    habitacion.reservar()
                    print(f"Reserva realizada a nombre de {cliente.nombre}.")
                    return
                else:
                    print(f"La habitación {numero_habitacion} ya está ocupada.")
                    return
        print(f"Hab. {numero_habitacion} no encontrada.")


# Uso del sistema de reservas
hotel = Hotel("Hotel Paraíso")
habitacion1 = Habitacion(101, "Individual", 50)
habitacion2 = Habitacion(102, "Doble", 80)

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

cliente1 = Cliente("Carlos Pérez", "0987654321")
cliente2 = Cliente("Ana García", "0981234567")

hotel.mostrar_habitaciones()
hotel.realizar_reserva(cliente1, 101)
hotel.realizar_reserva(cliente2, 101)
