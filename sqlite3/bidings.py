import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

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
    '(?, ?)'
)

# registrando valores nas colunas da tabela
# cursor.execute(sql, ['Richard', 14])
cursor.executemany(sql, [['Maria', 14], ['Wellington', 18]])
connection.commit()
print(sql)
cursor.close()
connection.close()
