# Programación Tradicional: Promedio semanal de temperaturas

def ingresar_temperaturas():
    """
    Solicita al usuario que ingrese temperaturas diarias durante una semana
    y las devuelve como una lista.
    """
    temperaturas = []
    print("Ingrese las temperaturas diarias:")
    for dia in range(1, 8):
        temp = float(input(f"Día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

def main():
    """
    Función principal que coordina la entrada de datos y el cálculo del promedio.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
