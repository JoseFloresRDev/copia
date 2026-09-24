import mysql.connector


DB_CONFIG = {
    "host": "172.31.18.158",
    "user": "flask_user",
    "password": "TuPasswordSegura",
    "database": "proyecto_flask",
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
