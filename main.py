import pymysql
import tkinter
from sql_queries.add_queries import *
from sql_queries.get_queries import *
from sql_queries.delete_queries import *
from sql_queries.update_queries import *


try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="", database="p314_test") as connection:
        print(connection, "ok")
        with connection.cursor() as cursor:
            # cursor.execute("""SHOW DATABASES""")        # сделать sql запрос
            # for db in cursor:
            #     print(*db)
            # sql_queries.add_student(cursor, connection)
            while True:
                print("1. Добавить студента.")
                print("2. Добавить группу.")
                print("3. Вывести всех студентов.")
                print("4. Вывести все группы.")
                print("0. Выход.")
                user_choice = input("Ваш выбор: ")
                match user_choice:
                    case "1":
                        values = get_students_from_console()
                        add_student(cursor, connection, values)
                    case "2":
                        values = get_groups_from_console()
                        add_group(cursor, connection, values)
                    case "3":
                        result = get_all_data(cursor, "students")
                        print(*result, sep="\n")
                    case "4":
                        pass
                    case "0":
                        break           # quit()
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