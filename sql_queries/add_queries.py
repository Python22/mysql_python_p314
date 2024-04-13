def get_students_from_console():
    return input("Имя: "), input("Фамилия: "), input("День рождения(2005-12-31): ")


def get_groups_from_console():
    return input("Название: "), input("Аудитория: "), int(input("Год начала обучения: "))


def add_student(cursor, connection, values):
   try:
       query = """
          INSERT INTO students (firstname, lastname, birthday) VALUES (%s, %s, %s)
          """
       cursor.execute(query, values)
       connection.commit()
       print("Студент добавлен. Его значения:", values)
   except:
       print("Студент не добавлен. Произошла ошибка")


def add_group(cursor, connection, values):
    try:
        query = """
        INSERT INTO groups (name, auditory, start_year) VALUES (%s, %s, %s)
        """
        cursor.execute(query, values)
        connection.commit()
        print("Группа добавлена. Её значения:", values)
    except:
        print("Группа не добавлена. Произошла ошибка")
