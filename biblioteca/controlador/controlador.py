from infra.conexion import ConexionDB
from modelo.libro import Libro


class ControladorLibro():
    def __init__(self):
        self.db = ConexionDB()
        
    def agregar_libro(self, libro:Libro):
        sql="INSERT INTO libros (titulo, autor, anio, categoria) VALUES (%s,%s,%s,%s)"
        valores = (libro.titulo, libro.autor, libro.anio, libro.categoria)
        self.db.cursor.execute(sql,valores)
        self.db.conn.commit()
        #recuperaremos el ultimo id registrado
        libro.id = self.db.cursor.lastrowid
        return libro #retorna el libro completo con su id asignada
    
    def listar_libros(self):
        sql = "SELECT * FROM libros"
        self.db.cursor.execute(sql)
        filas = self.db.cursor.fetchall()
        
        return [Libro (**fila) for fila in filas]
    
    def modificar_libro(self, libro:Libro):
        sql = "UPDATE libros SET titulo=%s, autor=%s, anio=%s, categoria=%s WHERE id=%s"
        valores = (libro.titulo, libro.autor, libro.anio, libro.categoria, libro.id )
        self.db.cursor.execute(sql,valores)
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0 #true
        
    def eliminar_libro(self, id_libro:int):
        sql="DELETE FROM libros WHERE id=%s"
        self.db.cursor.execute(sql,[id_libro])
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0 #true
    