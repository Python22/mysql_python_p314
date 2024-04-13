import pymysql
import sql_queries
import tkinter


try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="", database="p314_test") as connection:
        print(connection, "ok")
        with connection.cursor() as cursor:
            # cursor.execute("""SHOW DATABASES""")        # сделать sql запрос
            # for db in cursor:
            #     print(*db)
            # sql_queries.add_student(cursor, connection)
            print("1. Добавить студента.")
            print("2. Добавить группу.")
            user_choice = input("Ваш выбор: ")
            match user_choice:
                case "1":
                    values = sql_queries.get_students_from_console()
                    sql_queries.add_student(cursor, connection, values)
                case "2":
                    pass
                case _:
                    print("Неизвестная команда.")


except pymysql.Error as e:
    print(e)








#
# cursor.execute("""CREATE DATABASE IF NOT EXISTS p314_test""")
# cursor.execute("""USE p314_test""")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students
#     (
#     id int AUTO_INCREMENT PRIMARY KEY,
#     firstname VARCHAR(50),
#     lastname VARCHAR(50),
#     birthday DATE
#     )
# """)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS groups
#     (
#     id int AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(50),
#     auditory VARCHAR(50),
#     start_year INT
#     )
# """)