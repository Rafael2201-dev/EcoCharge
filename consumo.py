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

def listar_consumos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM consumo"
    cursor.execute(sql)

    consumos = cursor.fetchall()

    for consumo in consumos:
        print(consumo)

    conexao.close()

def listar_consumo_por_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM consumo WHERE id_usuario = %s"
    cursor.execute(sql, (id_usuario,))

    consumos = cursor.fetchall()

    for consumo in consumos:
        print(consumo)

    conexao.close()

def atualizar_consumo(id_consumo, tempo_uso=None, energia_consumida=None, data_consumo=None)   :
    conexao = conectar()
    cursor = conexao.cursor()

    campos_atualizacao = []
    valores = []

    if tempo_uso is not None:
            campos_atualizacao.append("tempo_uso = %s")
            valores.append(tempo_uso)

    if energia_consumida is not None:
            campos_atualizacao.append("energia_consumida = %s")
            valores.append(energia_consumida)

    if data_consumo is not None:
            campos_atualizacao.append("data_consumo = %s")
            valores.append(data_consumo)

    if not campos_atualizacao:
            print("Nenhum campo para atualizar.")
            return

    sql = f"UPDATE consumo SET {', '.join(campos_atualizacao)} WHERE id_consumo = %s"
    valores.append(id_consumo)

    cursor.execute(sql, tuple(valores))
    conexao.commit()

    print("Consumo atualizado!")

    conexao.close()

def excluir_consumo(id_consumo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM consumo WHERE id_consumo = %s"
    cursor.execute(sql, (id_consumo,))

    conexao.commit()

    print("Consumo excluído!")

    conexao.close()

