from conexao import conectar

def cadastrar_estacao(
    nome_estacao,
    localizacao,
    energia_disponivel,
    tomadas_disponiveis
):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO estacoes
    (
        nome_estacao,
        localizacao,
        energia_disponivel,
        tomadas_disponiveis
    )
    VALUES (%s, %s, %s, %s)
    """

    valores = (
        nome_estacao,
        localizacao,
        energia_disponivel,
        tomadas_disponiveis
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Estação cadastrada!")

    conexao.close()

# READ =========================

def listar_estacoes():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM estacoes"

    cursor.execute(sql)

    estacoes = cursor.fetchall()

    for estacao in estacoes:
        print(estacao)

    conexao.close()

# READ POR ID =========================

def buscar_estacao(id_estacao):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM estacoes
    WHERE id_estacao = %s
    """

    cursor.execute(sql, (id_estacao,))

    estacao = cursor.fetchone()

    print(estacao)

    conexao.close()

# UPDATE =========================

def atualizar_estacao(
    id_estacao,
    nome_estacao,
    localizacao,
    energia_disponivel,
    tomadas_disponiveis
):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE estacoes
    SET
        nome_estacao = %s,
        localizacao = %s,
        energia_disponivel = %s,
        tomadas_disponiveis = %s
    WHERE id_estacao = %s
    """

    valores = (
        nome_estacao,
        localizacao,
        energia_disponivel,
        tomadas_disponiveis,
        id_estacao
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Estação atualizada!")

    conexao.close()


# DELETE =========================

def deletar_estacao(id_estacao):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM estacoes
    WHERE id_estacao = %s
    """

    cursor.execute(sql, (id_estacao,))

    conexao.commit()

    print("Estação deletada!")

    conexao.close()