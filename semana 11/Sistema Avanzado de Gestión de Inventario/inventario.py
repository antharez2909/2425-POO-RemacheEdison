import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID ya existe.")
            return False
        self.productos[producto.get_id()] = producto
        return True

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            return True
        else:
            print("Error: Producto no encontrado.")
            return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if not producto:
            print("Error: Producto no encontrado.")
            return False
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)
        return True

    def buscar_por_nombre(self, nombre):
        nombre = nombre.lower()
        return [p for p in self.productos.values() if nombre in p.get_nombre().lower()]

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    def guardar_en_archivo(self, archivo):
        datos = [producto.to_dict() for producto in self.productos.values()]
        try:
            with open(archivo, 'w') as f:
                json.dump(datos, f, indent=4)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            nuevos_productos = {}
            for item in datos:
                try:
                    id = str(item['id'])
                    nombre = item['nombre']
                    cantidad = int(item['cantidad'])
                    precio = float(item['precio'])
                except KeyError as e:
                    print(f"Error: Falta clave {e} en el ítem.")
                    continue
                except (ValueError, TypeError) as e:
                    print(f"Error en datos del producto {id}: {e}")
                    continue
                if id in nuevos_productos:
                    print(f"Error: ID duplicado {id}.")
                    continue
                producto = Producto(id, nombre, cantidad, precio)
                nuevos_productos[id] = producto
            self.productos = nuevos_productos
            return True
        except FileNotFoundError:
            print("Archivo no encontrado. Creando nuevo inventario.")
            return False
        except json.JSONDecodeError:
            print("Error: Formato de archivo inválido.")
            return False
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False

def main():
    inventario = Inventario()
    archivo = "inventario.json"

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del producto: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: Cantidad debe ser entero y precio decimal.")
                continue
            if cantidad < 0 or precio < 0:
                print("Error: Valores no pueden ser negativos.")
                continue
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("Producto añadido.")
            else:
                print("Error al añadir.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ").strip()
            cantidad = input("Nueva cantidad (vacío para omitir): ").strip()
            precio = input("Nuevo precio (vacío para omitir): ").strip()
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            if inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio):
                print("Producto actualizado.")
            else:
                print("Error al actualizar.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            if inventario.guardar_en_archivo(archivo):
                print("Inventario guardado.")
            else:
                print("Error al guardar.")

        elif opcion == "7":
            if inventario.cargar_desde_archivo(archivo):
                print("Inventario cargado.")
            else:
                print("Error al cargar.")

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()