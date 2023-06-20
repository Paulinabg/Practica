import sqlite3

def test_connection():
    try:
        conn = sqlite3.connect('gestor_password.db')
        conn.execute('SELECT 1')
        print("Conexión exitosa a la base de datos")
        conn.close()
    except sqlite3.Error as error:
        print("Error al conectar a la base de datos:", error)

# Llamada a la función para probar la conexión
test_connection()
