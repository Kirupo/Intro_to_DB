# MySQLServer.py

import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
