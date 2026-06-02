import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="mysql://root:cGHlnwhsZwrXZarwFzuNHSUjSjMzLiuC@acela.proxy.rlwy.net:12056/railway",
        user="root",
        password="cGHlnwhsZwrXZarwFzuNHSUjSjMzLiuC",
        database="railway"
    )

    return conexao