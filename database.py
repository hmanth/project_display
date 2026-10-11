
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2005",
        database="product_db"
    )

    return connection
