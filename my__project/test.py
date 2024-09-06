import sqlite3
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT, total_score INTEGER DEFAULT 0)')
    print("Table created successfully")
    conn.close()
    
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT username, total_score FROM users")
users = cursor.fetchall()

print(users)