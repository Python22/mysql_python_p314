import pymysql


try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="") as connection:
        print(connection, "ok")
        with connection.cursor() as cursor:
            cursor.execute("""SHOW DATABASES""")
            for i in cursor:
                print(i)

except pymysql.Error as e:
    print(e)
