import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2201",
        database="ecocharge"
    )

    return conexao