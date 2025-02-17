from producto import Producto  # Importa la clase Producto desde producto.py

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []  # Lista para almacenar objetos Producto

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.

        Args:
            producto (Producto): El objeto Producto a agregar.
        """
        # Verifica si ya existe un producto con ese ID
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("¡Error! Ya existe un producto con ese ID.")
            return

        self.productos.append(producto)  # Añade el producto a la lista

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.

        Args:
            id_producto (int): El ID del producto a eliminar.
        """
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id_producto:
                del self.productos[i]  # Elimina el producto de la lista
                print("Producto eliminado.")
                return

        print("¡Error! No existe un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto por su ID.

        Args:
            id_producto (int): El ID del producto a actualizar.
            cantidad (int, opcional): La nueva cantidad del producto.
            precio (float, opcional): El nuevo precio del producto.
        """
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad  # Actualiza la cantidad
                if precio is not None:
                    producto.precio = precio  # Actualiza el precio
                print("Producto actualizado.")
                return

        print("¡Error! No existe un producto con ese ID.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (puede haber coincidencias parciales).

        Args:
            nombre (str): El nombre a buscar.

        Returns:
            list: Una lista con los productos que coinciden con el nombre.
        """
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():  # Búsqueda insensible a mayúsculas
                resultados.append(producto)

        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)  # Imprime la representación __str__ de cada producto

# Ejemplo de uso (puedes mover esto a otro archivo o dejarlo aquí para probar)
inventario = Inventario()
producto1 = Producto(1, "Camiseta", 10, 20.00)
inventario.agregar_producto(producto1)
inventario.mostrar_inventario()