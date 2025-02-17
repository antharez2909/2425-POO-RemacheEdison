class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Args:
            id_producto (int): El ID único del producto.
            nombre (str): El nombre del producto.
            cantidad (int): La cantidad en stock del producto.
            precio (float): El precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters (métodos para acceder y modificar los atributos)
    def get_id(self):
        """
        Obtiene el ID del producto.

        Returns:
            int: El ID del producto.
        """
        return self.id_producto

    def set_id(self, id_producto):
        """
        Establece el ID del producto.

        Args:
            id_producto (int): El nuevo ID del producto.
        """
        self.id_producto = id_producto

    # ... (Getters y setters para nombre, cantidad y precio)

    def __str__(self):
        """
        Representación en cadena del objeto Producto.

        Returns:
            str: Una cadena con la información del producto.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"