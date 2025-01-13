## Programa para calcular el área de un círculo
# El usuario ingresa el radio y el programa calcula el área utilizando la fórmula: área = π * radio^2

import math  # Importamos el módulo para operaciones matemáticas

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo (número flotante)
    :return: El área del círculo (número flotante)
    """
    area = math.pi * radio ** 2  # Fórmula para el área del círculo
    return area

# Solicitar al usuario el radio del círculo
radio_usuario = float(input("Introduce el radio del círculo: "))  # Convertimos la entrada a un número flotante

# Calcular el área utilizando la función
area_circulo = calcular_area_circulo(radio_usuario)

# Mostrar el resultado
print(f"El área del círculo con radio {radio_usuario} es: {area_circulo:.2f}")

