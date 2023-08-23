import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    passwd=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"]
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
        print(sql)
        print(data1)
        print(result)
    connection.commit()
