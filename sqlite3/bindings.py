import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"DELETE FROM {TABLE_NAME}"
)

# criação de tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)

# registrando valores nas colunas da tabela
# cursor.execute(sql, {'name': 'Rian', 'weight': 20})
cursor.executemany(sql, (
    {'name': 'Joao', 'weight': 7},
    {'name': 'Pedro', 'weight': 3},
    {'name': 'Carlos', 'weight': 1},
    {'name': 'Felipe', 'weight': 11}
    )
)
connection.commit()
print(sql)
cursor.close()
connection.close()
