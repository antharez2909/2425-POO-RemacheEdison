class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor de la clase Producto. Inicializa los atributos de un producto.
        self.id = id  # Identificador único del producto.
        self.nombre = nombre  # Nombre del producto.
        self.cantidad = cantidad  # Cantidad disponible en el inventario.
        self.precio = precio  # Precio del producto.

    def __str__(self):
        # Método especial para representar el objeto como una cadena de texto.
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Constructor de la clase Inventario. Inicializa el inventario y carga los productos desde un archivo.
        self.archivo = archivo  # Nombre del archivo donde se guarda el inventario.
        self.productos = []  # Lista para almacenar los productos.
        self.cargar_inventario()  # Llama al método para cargar el inventario desde el archivo.

    def cargar_inventario(self):
        # Método para cargar los productos desde el archivo de texto.
        try:
            with open(self.archivo, 'r') as file:  # Abre el archivo en modo lectura.
                for linea in file:  # Itera sobre cada línea del archivo.
                    # Divide la línea en partes usando la coma como separador.
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    # Crea un objeto Producto con los datos de la línea.
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)  # Añade el producto a la lista.
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno nuevo.
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            open(self.archivo, 'w').close()  # Crea un archivo vacío.
        except Exception as e:
            # Captura cualquier otro error y muestra un mensaje.
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        # Método para guardar los productos en el archivo de texto.
        try:
            with open(self.archivo, 'w') as file:  # Abre el archivo en modo escritura.
                for producto in self.productos:  # Itera sobre cada producto en la lista.
                    # Escribe los datos del producto en el archivo, separados por comas.
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            # Si no hay permisos para escribir en el archivo, muestra un mensaje de error.
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            # Captura cualquier otro error y muestra un mensaje.
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        # Método para añadir un nuevo producto al inventario.
        self.productos.append(producto)  # Añade el producto a la lista.
        self.guardar_inventario()  # Guarda los cambios en el archivo.
        print(f"Producto '{producto.nombre}' añadido exitosamente.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Método para actualizar la cantidad o el precio de un producto existente.
        for producto in self.productos:  # Itera sobre cada producto en la lista.
            if producto.id == id:  # Busca el producto con el ID especificado.
                if cantidad is not None:  # Si se proporciona una nueva cantidad, actualiza.
                    producto.cantidad = cantidad
                if precio is not None:  # Si se proporciona un nuevo precio, actualiza.
                    producto.precio = precio
                self.guardar_inventario()  # Guarda los cambios en el archivo.
                print(f"Producto ID {id} actualizado exitosamente.")
                return  # Sale del método después de actualizar.
        print(f"Error: Producto con ID {id} no encontrado.")  # Si no se encuentra el producto, muestra un mensaje.

    def eliminar_producto(self, id):
        # Método para eliminar un producto del inventario.
        # Crea una nueva lista excluyendo el producto con el ID especificado.
        self.productos = [p for p in self.productos if p.id != id]
        self.guardar_inventario()  # Guarda los cambios en el archivo.
        print(f"Producto ID {id} eliminado exitosamente.")

    def listar_productos(self):
        # Método para listar todos los productos en el inventario.
        if not self.productos:  # Si no hay productos, muestra un mensaje.
            print("El inventario está vacío.")
        else:
            for producto in self.productos:  # Itera sobre cada producto y lo imprime.
                print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crea una instancia de la clase Inventario.
    inventario = Inventario()

    # Añade productos al inventario.
    inventario.añadir_producto(Producto(1, "Pan Integral", 50, 2.50))
    inventario.añadir_producto(Producto(2, "Croissant", 30, 1.80))

    # Lista todos los productos en el inventario.
    inventario.listar_productos()

    # Actualiza la cantidad del producto con ID 1.
    inventario.actualizar_producto(1, cantidad=40)

    # Elimina el producto con ID 2.
    inventario.eliminar_producto(2)

    # Lista todos los productos después de las modificaciones.
    inventario.listar_productos()