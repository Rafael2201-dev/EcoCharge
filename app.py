from flask import Flask, render_template, request
from usuario import cadastrar_usuario

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        tipo = request.form["tipo"]

        cadastrar_usuario(
            nome,
            email,
            senha,
            tipo
        )

        return "Usuário cadastrado com sucesso!"

    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug=True)