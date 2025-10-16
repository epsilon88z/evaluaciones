import mysql.connector

class ConexionDB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="libreria666s"
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("Conexion a MySQL Correcta")
        except mysql.connector.Error as e:
            print(f'Error de conexion: {e}')