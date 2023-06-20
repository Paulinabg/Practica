import hashlib
import sqlite3

DATABASE = 'gestor_password.db'

def create_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def validate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = cursor.fetchone()
    conn.close()

    if user is not None:
        return True
    else:
        return False

# Crear usuarios
create_user("Paulina", "cisco123")
create_user("Matías", "cisco123")

# Validar usuarios
login_username = input('Ingrese el nombre de usuario para iniciar sesión: ')
login_password = input('Ingrese la contraseña para iniciar sesión: ')

if validate_user(login_username, login_password):
    print('Inicio de sesión exitoso')
else:
    print('Nombre de usuario o contraseña inválidos')
