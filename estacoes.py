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