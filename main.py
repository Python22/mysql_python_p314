import pymysql


try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="") as connection:
        print(connection, "ok")
        with connection.cursor() as cursor:
            cursor.execute("""SHOW DATABASES""")        # сделать sql запрос
            for db in cursor:
                print(*db)

            cursor.execute("""CREATE DATABASE IF NOT EXISTS p314_test""")
            cursor.execute("""USE p314_test""")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students
                (
                id int AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(50),
                lastname VARCHAR(50),
                birthday DATE
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS groups
                (
                id int AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                auditory VARCHAR(50),
                start_year INT
                )
            """)


except pymysql.Error as e:
    print(e)
