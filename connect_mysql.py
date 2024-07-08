import mysql.connector
from mysql.connector import Error 



# connecting to the database 

def connect_db():
    db_name = "e_LMS_db"
    user = "root"
    password = "SydneyARCHTsql1!" # CHANGE PASSWORD!!
    host = "localhost"
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        if conn.is_connected():# checking the successful connection
            print("Connected to MySQL Database successfully")
            return conn
    except Error as e:
        print(f"Error: {e}")

    # finally: #succesfully tested and closed out
    #     # closing the connection
    #     if conn and conn.is_connected():
    #         conn.close()
    #         print("MySql Connection is closed.")

connect_db()