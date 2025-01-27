class ConexionBD:
    # Constructor (__init__): inicializa la conexión a la base de datos
    def __init__(self, servidor, base_datos):
        self.servidor = servidor
        self.base_datos = base_datos
        self.conexion = None
        self.conectar()

    # Método para simular la conexión a una base de datos
    def conectar(self):
        if not self.conexion:
            self.conexion = f"Conexión exitosa al servidor {self.servidor}, base de datos: {self.base_datos}"
            print(self.conexion)

    # Destructor (__del__): realiza la desconexión de la base de datos
    def __del__(self):
        if self.conexion:
            print(f"Desconectando de la base de datos {self.base_datos} en el servidor {self.servidor}")
            self.conexion = None

# Crear un objeto de la clase ConexionBD
conexion = ConexionBD("localhost", "mi_base_de_datos")

# Simular la eliminación del objeto (destrucción de la conexión)
del conexion  # Llamada explícita al destructor

# Python también llamará al destructor cuando el objeto salga del alcance
