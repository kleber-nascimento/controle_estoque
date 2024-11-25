import sqlite3
from config import DATABASE_URI

# Configuração do banco de dados
def init_db():
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
            users (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            cpf TEXT NOT NULL,
            phone TEXT NOT NULL,
        )
''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URI)
    return conn