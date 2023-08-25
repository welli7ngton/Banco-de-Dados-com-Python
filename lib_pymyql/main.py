import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    passwd=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # TRUNCATE TABLE APAGA A TABELA POR COMPLETO
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES(%(name)s, %(age)s) '
        )
        data = (
            {
                "name": "Luiz",
                "age": 27
            },            {
                "name": "Wellington",
                "age": 20
            },            {
                "name": "Roger",
                "age": 14
            },            {
                "name": "Pedro",
                "age": 19
            },

        )
        result = cursor.executemany(sql, data)
        # print(sql)
        # print(data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES(%s, %s) '
        )
        data1 = (
            ("maria", 18), ("raimundo", 78)
        )
        result = cursor.executemany(sql, data1)
        # print(sql)
        # print(data1)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        # menor_id = input("digite o menor id: ")
        # maior_id = input("digite o maior id: ")
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id >= %s AND id <= %s'
        )

        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))

        data2 = cursor.fetchall()

        # for value in data2:
        #     print(value)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )

        # cursor.execute(sql, (1))
        # cursor.execute(sql, (2))
        # cursor.execute(sql, (3))
        # connection.commit()

        # cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for value in cursor.fetchall():
        #     print(value)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )

        # cursor.execute(sql, ("teste", 99, 1))
        # connection.commit()
        # cursor.execute(sql, ("RAIMUNDO", 75, 6))
        # connection.commit()

        # cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for value in cursor.fetchall():
        #     print(value)

    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for value in cursor.fetchall():
            print(value)
