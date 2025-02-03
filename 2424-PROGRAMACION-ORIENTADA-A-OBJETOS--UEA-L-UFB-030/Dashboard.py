import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()




# MEJORAS POR PARTE DE EDISON REMACHE
import os
import subprocess
import linecache  # Para mostrar números de línea

def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_codigo(ruta_script):
    """Muestra el código de un script con descripción y números de línea."""
    try:
        with open(ruta_script, 'r') as archivo:
            linea = archivo.readline()
            if linea.startswith("# :"):
                descripcion = linea[3:].strip()  # Extrae la descripción del comentario
                print(f"\nDescripción: {descripcion}\n")

            codigo = archivo.read()

            print(f"Código de {ruta_script}:\n")

            for num, linea in enumerate(codigo.splitlines(), 1):
                print(f"{num:4}: {linea}")  # Imprime el número de línea y el código

            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script y maneja posibles errores."""
    try:
        if os.name == 'nt':  # Windows
            proceso = subprocess.Popen(['cmd', '/k', 'python', ruta_script], stderr=subprocess.PIPE)
        else:  # Unix-based systems (xterm es un ejemplo, puedes usar otra terminal)
            proceso = subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script], stderr=subprocess.PIPE)

        stdout, stderr = proceso.communicate()  # Captura la salida y errores del script

        if stderr:
            print(f"Error al ejecutar el script:\n{stderr.decode()}")  # Imprime errores si existen
        else:
            print(stdout.decode())  # Imprime la salida del script si no hay errores

    except FileNotFoundError:
        print(f"Error: No se encontró el script en {ruta_script}")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """Muestra el menú principal."""
    limpiar_pantalla()  # Limpia la pantalla al mostrar el menú

    # ... (resto del código sin cambios)

def mostrar_sub_menu(ruta_unidad):
   """Muestra el submenú de carpetas."""
   limpiar_pantalla()  # Limpia la pantalla al mostrar el submenú

   # ... (resto del código sin cambios)

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra la lista de scripts y permite ver/ejecutar."""
    limpiar_pantalla()  # Limpia la pantalla al mostrar la lista de scripts

    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            ruta_completa = os.path.join(ruta_sub_carpeta, script)  # Obtiene la ruta completa
            print(f"{i} - {ruta_completa}")  # Muestra la ruta completa

        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")
        print("E - Ejecutar script sin ver el código")  # Opción para ejecutar sin ver

        eleccion_script = input("Elige un script, '0' para regresar, '9' para ir al menú principal o 'E' para ejecutar: ")

        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        elif eleccion_script == 'E':  # Ejecutar sin ver
            try:
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[int(eleccion_script) - 1])
                ejecutar_codigo(ruta_script)
            except (ValueError, IndexError):
                print("Opción no válida.")
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")

                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()