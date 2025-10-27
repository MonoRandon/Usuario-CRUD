from flask_app.config.mysqlconnection import MySQLConnection

# Nombre de la base de datos 
BASE_DATOS = 'esquema_t'


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Crear usuario
    @classmethod
    def guardar(cls, data):
        query = """
        INSERT INTO usuarios (nombre, email, edad, created_at, updated_at)
        VALUES (%(nombre)s, %(email)s, %(edad)s, NOW(), NOW());
        """
        conexion = MySQLConnection(BASE_DATOS)
        return conexion.query_db(query, data)

    # Obtener todos
    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios;"
        conexion = MySQLConnection(BASE_DATOS)
        resultados = conexion.query_db(query)
        return [cls(usuario) for usuario in resultados]

    # Obtener uno por id
    @classmethod
    def obtener_uno(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        conexion = MySQLConnection(BASE_DATOS)
        resultado = conexion.query_db(query, data)
        if len(resultado) == 0:
            return None
        return cls(resultado[0])

    # Actualizar usuario
    @classmethod
    def actualizar(cls, data):
        query = """
        UPDATE usuarios
        SET nombre=%(nombre)s, email=%(email)s, edad=%(edad)s, updated_at=NOW()
        WHERE id=%(id)s;
        """
        conexion = MySQLConnection(BASE_DATOS)
        return conexion.query_db(query, data)

    # Eliminar usuario
    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM usuarios WHERE id=%(id)s;"
        conexion = MySQLConnection(BASE_DATOS)
        return conexion.query_db(query, data)
