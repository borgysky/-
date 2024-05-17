import psycopg2


def connect(db_name, db_user, db_password, db_host, db_port):
    global connection
    try:
        connection = psycopg2.connect(database=db_name, 
                                      user=db_user, 
                                      password=db_password, 
                                      host=db_host, 
                                      port=db_port)
        print("we're so back")

    except Exception as e:
        print("error")
    return connection

connect("art school", "postgres", "postgresql", "localhost", "5432")

        # with connection.cursor() as cursor:
        #     cursor.execute("select * from groups")
        #     print(f"data: {cursor.fetchall()}")

def view_entry():
    cursor = connection.cursor()
    query = "select * from groups"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
view_entry()

