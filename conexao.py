import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="acela.proxy.rlwy.net",
        user="root",
        password="cGHlnwhsZwrXZarwFzuNHSUjSjMzLiuC",
        database="railway",
        port=12056
    )

    return conexao