# Ejemplo de aplicación de conceptos de POO en Python

# Clase base que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público
        self.__velocidad = 0  # Atributo privado (encapsulación)

    def arrancar(self):
        return f"El vehículo {self.marca} {self.modelo} está arrancado."

    def acelerar(self, incremento):
        if incremento > 0:
            self.__velocidad += incremento
        return f"El vehículo ahora va a {self.__velocidad} km/h."

    def obtener_velocidad(self):
        return self.__velocidad

# Clase derivada que representa un coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.puertas = puertas  # Atributo propio de la clase derivada

    # Sobrescritura de un método (Polimorfismo)
    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} con {self.puertas} puertas está listo para conducir."

# Clase derivada que representa una moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Tipo de moto (e.g., deportiva, urbana)

    # Sobrescritura del método arrancar (Polimorfismo)
    def arrancar(self):
        return f"La moto {self.marca} {self.modelo} de tipo {self.tipo} está lista para rodar."

# Ejemplo de uso de las clases e instancias
if __name__ == "__main__":
    # Crear objetos de las clases
    vehiculo = Vehiculo("Genérico", "ModeloX")
    coche = Coche("Toyota", "Corolla", 4)
    moto = Moto("Yamaha", "R1", "Deportiva")

    # Demostración de funcionalidad
    print(vehiculo.arrancar())  # Método de la clase base
    print(coche.arrancar())     # Sobrescritura en la clase derivada Coche
    print(moto.arrancar())      # Sobrescritura en la clase derivada Moto

    print(vehiculo.acelerar(20))  # Incremento de velocidad del vehículo genérico
    print(f"Velocidad actual: {vehiculo.obtener_velocidad()} km/h")
