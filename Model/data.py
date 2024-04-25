import sqlite3

class BaseDatos:
    def __init__(self,data):
        self.data = data

    def crear_tabla(self):
        conexion = sqlite3.connect(self.data)
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                   id INTEGER PRIMARY KEY,
                   codigo TEXT UNIQUE,
                   nombre TEXT NOT NULL,
                   cantidad INTEGER NOT NULL
    )''')
        conexion.commit()
        conexion.close()

    def agregar_productos(self, codigo,nombre, cantidad):
         conexion = sqlite3.connect(self.data)
         cursor= conexion.cursor()
         cursor.execute("INSERT INTO productos (codigo, nombre, cantidad) VALUES (?,?,?)",(codigo,nombre,cantidad ))
         conexion.commit()
         conexion.close()
        
    def listar_productos(self):
        conexion = sqlite3.connect(self.data)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos
    
    def eliminar_productos(self, codigo):
        conexion = sqlite3.connect(self.data)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        rows_affected = conexion.total_changes  # Obtiene el número de filas afectadas
        conexion.commit()
        conexion.close()
        return rows_affected > 0  # Devuelve True si se eliminó alguna fila, False en caso contrario

if __name__== "__main__":
    try:
       db = BaseDatos ('data.db')
       db.crear_tabla() 
       print("Exito")
    except Exception as e:
        print("Error")