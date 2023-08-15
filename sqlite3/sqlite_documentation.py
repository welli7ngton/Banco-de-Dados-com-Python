import sqlite3

# Criando conexão
connection = sqlite3.connect('./sqlite3/test.sqlite3')
# Criando cursor para realizar as consultas SQL
cursor = connection.cursor()

cursor.execute(
    "DELETE FROM movie"
)

cursor.execute(
    'CREATE TABLE IF NOT EXISTS movie(title, year, score)'
)

result = cursor.execute('SELECT name FROM sqlite_master')
print(result.fetchone())

# Caso a consulta seja feita em uma tabela que não
# existe o .fetchone() vai retornar None.
result = cursor.execute('SELECT name FROM sqlite_master WHERE name="spam"')
print(result.fetchone() is None)

cursor.execute("""
    INSERT INTO movie VALUES
               ('Monty Oython and the Holy Grail', 1975, 8.2),
               ('And Now for Something Completely Different', 1971, 7.5)
""")

# O estado de INSERT implicitamente abre uma transação, que 
# precisa ser commitada antes que as alterações sejam salvas no 
# banco de dados. Use .commit() no objeto de conexão para commitar
# a transação
connection.commit()

result = cursor.execute("SELECT score FROM movie")
print(result.fetchall())

result = cursor.execute("SELECT title FROM movie")
print(result.fetchall())

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0)
]

cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
connection.commit()
