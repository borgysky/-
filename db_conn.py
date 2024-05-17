import psycopg2


def connect(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(database=db_name, 
                                      user=db_user, 
                                      password=db_password, 
                                      host=db_host, 
                                      port=db_port)
        print("we're so back")
        connection.autocommit = True

    except Exception as e:
        print("error")
    return connection


def check_columns(connection, table_name):
    try:
        with connection.cursor() as cursor:
            column_name_query = f"""
                               SELECT column_name
                               FROM information_schema.columns
                               WHERE table_name = '{table_name}'
                               ORDER BY ordinal_position ASC;
                           """
            cursor.execute(column_name_query)
            columns = cursor.fetchall()
            column_names = [col[0] for col in columns]
            return column_names
    except Exception as e:
        print(f"The error '{e}' occurred")
        return None

def add_entry(connection, table_name, data):
    try:
        with connection.cursor() as cursor:
            user_records = ", ".join(["%s"] * len(data))
            column_names = check_columns(connection, table_name)
            insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES {user_records}"
            cursor.execute(insert_query, data)
            print(insert_query)
    except Exception as e:
        print(f"The error '{e}' occurred")