import mysql.connector

try:
    db_connection = mysql.connector.connect(
        host='ec-daemon-db-1',
        user='user',
        password='password',
        port='3306'
    )

    if db_connection.is_connected:
        print("Connected!")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    if db_connection is not None and db_connection.is_connected:
        db_connection.close()