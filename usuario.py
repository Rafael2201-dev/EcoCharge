from conexao import conectar

def cadastrar_usuario(nome, email, senha, tipo_usuario):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuarios
    (nome, email, senha, tipo_usuario)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nome, email, senha, tipo_usuario)

    cursor.execute(sql, valores)

    conexao.commit()

    print("Usuário cadastrado!")

    conexao.close()


# READ =========================

def listar_usuarios():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM usuarios"

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(usuario)

    conexao.close()

# READ POR ID =========================

def buscar_usuario(id_usuario):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM usuarios
    WHERE id_usuario = %s
    """

    cursor.execute(sql, (id_usuario,))

    usuario = cursor.fetchone()

    print(usuario)

    conexao.close()

# UPDATE =========================

def atualizar_usuario(
    id_usuario,
    nome,
    email,
    senha,
    tipo_usuario
):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE usuarios
    SET
        nome = %s,
        email = %s,
        senha = %s,
        tipo_usuario = %s
    WHERE id_usuario = %s
    """

    valores = (
        nome,
        email,
        senha,
        tipo_usuario,
        id_usuario
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Usuário atualizado!")

    conexao.close()

# DELETE =========================

def deletar_usuario(id_usuario):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM usuarios
    WHERE id_usuario = %s
    """

    cursor.execute(sql, (id_usuario,))

    conexao.commit()

    print("Usuário deletado!")

    conexao.close()