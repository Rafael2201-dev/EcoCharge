from conexao import conectar

def registrar_consumo(
    id_usuario,
    id_estacao,
    tempo_uso,
    energia_consumida,
    data_consumo
):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO consumo
    (
        id_usuario,
        id_estacao,
        tempo_uso,
        energia_consumida,
        data_consumo
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        id_usuario,
        id_estacao,
        tempo_uso,
        energia_consumida,
        data_consumo
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Consumo registrado!")

    conexao.close()