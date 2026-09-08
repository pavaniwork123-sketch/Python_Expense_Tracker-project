from pymysql import connect
def create_connection():
    connection=connect(
        host="localhost",
        user="root",
        password="Pavani@123",
        database="expenses"
    )
    return connection

