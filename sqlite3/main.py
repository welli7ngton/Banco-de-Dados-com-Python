import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'wheigt REAL'
    ')'
)

connection.commit()

cursor.close()
connection.close()
