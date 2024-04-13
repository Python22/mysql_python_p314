def get_all_data(cursor, table):
    query = f"""SELECT * FROM {table}"""
    cursor.execute(query)
    result = []
    for i in cursor:
        result.append(i)
    return result
