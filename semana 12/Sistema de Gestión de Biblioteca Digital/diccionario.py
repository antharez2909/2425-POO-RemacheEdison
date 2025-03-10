
class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Atributos:
        titulo_autor (tuple): Tupla que contiene el título y el autor del libro (inmutables).
        categoria (str): Categoría del libro.
        isbn (str): ISBN del libro (único).
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]} (ISBN: {self.isbn})"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Atributos:
        nombre (str): Nombre del usuario.
        id_usuario (str): ID único del usuario.
        libros_prestados (list): Lista de libros actualmente prestados al usuario.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    """
    Clase que gestiona la biblioteca digital.
    Atributos:
        libros (dict): Diccionario que almacena los libros disponibles, con ISBN como clave.
        usuarios_registrados (set): Conjunto de IDs de usuarios registrados.
        prestamos (dict): Diccionario que almacena el historial de préstamos (ID usuario: lista de libros prestados).
    """
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para IDs de usuarios únicos
        self.prestamos = {}  # Diccionario para historial de préstamos

    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.
        Parámetros:
            libro (Libro): Objeto de la clase Libro.
        """
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")

    def quitar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca.
        Parámetros:
            isbn (str): ISBN del libro a eliminar.
        """
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.
        Parámetros:
            usuario (Usuario): Objeto de la clase Usuario.
        """
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.prestamos[usuario.id_usuario] = []
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_de_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario de la biblioteca.
        Parámetros:
            id_usuario (str): ID del usuario a dar de baja.
        """
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.prestamos[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro a un usuario.
        Parámetros:
            id_usuario (str): ID del usuario al que se presta el libro.
            isbn (str): ISBN del libro a prestar.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros:
            print(f"No se encontró un libro con ISBN {isbn}.")
        else:
            libro = self.libros[isbn]
            self.prestamos[id_usuario].append(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {id_usuario}.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Devuelve un libro prestado por un usuario.
        Parámetros:
            id_usuario (str): ID del usuario que devuelve el libro.
            isbn (str): ISBN del libro a devolver.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros:
            print(f"No se encontró un libro con ISBN {isbn}.")
        else:
            libros_prestados = self.prestamos[id_usuario]
            libro = self.libros[isbn]
            if libro in libros_prestados:
                libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo_autor[0]}' devuelto por {id_usuario}.")
            else:
                print(f"El libro con ISBN {isbn} no estaba prestado a {id_usuario}.")

    def buscar_libro_por_titulo(self, titulo):
        """
        Busca libros por título.
        Parámetros:
            titulo (str): Título del libro a buscar.
        """
        resultados = [libro for libro in self.libros.values() if libro.titulo_autor[0].lower() == titulo.lower()]
        if resultados:
            print(f"Resultados para '{titulo}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_libro_por_autor(self, autor):
        """
        Busca libros por autor.
        Parámetros:
            autor (str): Autor del libro a buscar.
        """
        resultados = [libro for libro in self.libros.values() if libro.titulo_autor[1].lower() == autor.lower()]
        if resultados:
            print(f"Resultados para libros de '{autor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")

    def buscar_libro_por_categoria(self, categoria):
        """
        Busca libros por categoría.
        Parámetros:
            categoria (str): Categoría del libro a buscar.
        """
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        if resultados:
            print(f"Resultados para la categoría '{categoria}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros en la categoría '{categoria}'.")

    def listar_libros_prestados(self, id_usuario):
        """
        Lista los libros prestados a un usuario.
        Parámetros:
            id_usuario (str): ID del usuario.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        else:
            libros_prestados = self.prestamos[id_usuario]
            if libros_prestados:
                print(f"Libros prestados a {id_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"El usuario {id_usuario} no tiene libros prestados.")


# Pruebas del sistema
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-0307350487")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0451524935")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "978-0156012195")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("María López", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", "978-0307350487")
    biblioteca.prestar_libro("002", "978-0451524935")

    # Buscar libros
    biblioteca.buscar_libro_por_titulo("1984")
    biblioteca.buscar_libro_por_autor("Gabriel García Márquez")
    biblioteca.buscar_libro_por_categoria("Fábula")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")
    biblioteca.listar_libros_prestados("002")

    # Devolver libros
    biblioteca.devolver_libro("001", "978-0307350487")
    biblioteca.listar_libros_prestados("001")

    # Dar de baja a un usuario
    biblioteca.dar_de_baja_usuario("002")
    biblioteca.listar_libros_prestados("002")