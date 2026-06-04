import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="acela.proxy.rlwy.net",
        user="root",
        password="cGHlnwhsZwrXZarwFzuNHSUjSjMzLiuC",
        database="ecocharge",
        port=12056
    )

    return conexao