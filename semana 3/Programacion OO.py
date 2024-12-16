# Programación Orientada a Objetos: Promedio semanal de temperaturas

class ClimaSemanal:
    """
    Clase para manejar las temperaturas diarias y calcular el promedio semanal.
    """
    def __init__(self):
        # Atributo privado para almacenar las temperaturas
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        print("Ingrese las temperaturas diarias:")
        for dia in range(1, 8):
            temp = float(input(f"Día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las temperaturas semanales.
        """
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        """
        Método para mostrar el promedio semanal.
        """
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")


# Bloque principal
if __name__ == "__main__":
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()
