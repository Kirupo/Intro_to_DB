# File: MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host='localhost',   # change if your server is remote or has a different host
            user='root',        # change to your MySQL username
            password=''         # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            cursor.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
