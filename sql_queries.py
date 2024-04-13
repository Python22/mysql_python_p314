import pymysql


def get_students_from_console():
    return input("Имя: "), input("Фамилия: "), input("День рождения(2005-12-31): ")


def add_student(cursor, connection, values):
    query = """
    INSERT INTO students (firstname, lastname, birthday) VALUES (%s, %s, %s)
    """
    cursor.execute(query, values)
    connection.commit()
    print("Студент добавлен. Его значения:", values)


def add_group(cursor, connection):
    pass
