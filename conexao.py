import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2201",
    database="ecocharge"
)
print("Conectado!")

cursor = conexao.cursor()


sql = """
INSERT INTO usuarios (nome, email, senha, tipo_usuario)
VALUES (%s, %s, %s, %s)
"""

valores = (
    "Rafael",
    "rafa@email.com",
    "123456",
    "cliente"
)

cursor.execute(sql, valores)

conexao.commit()

print("Usuário cadastrado!")


sql = """
INSERT INTO estacoes (
    nome_estacao,
    localizacao,
    energia_disponivel,
    tomadas_disponiveis
)
VALUES (%s, %s, %s, %s)
"""

valores = (
    "EcoCharge Centro",
    "Campinas-SP",
    85.5,
    6
)

cursor.execute(sql, valores)

conexao.commit()

print("Estação cadastrada!")


sql = """
INSERT INTO consumo (
    id_usuario,
    id_estacao,
    tempo_uso,
    energia_consumida,
    data_consumo
)
VALUES (%s, %s, %s, %s, %s)
"""

valores = (
    1,              # usuário
    1,              # estação
    45,             # minutos
    2.5,            # kWh
    "2026-05-19"
)

cursor.execute(sql, valores)

conexao.commit()

print("Consumo registrado!")