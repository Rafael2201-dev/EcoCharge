CREATE DATABASE ecocharge;

USE ecocharge;

-- Tabela de users
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(50),
    tipo_usuario VARCHAR(20)
);

-- Tabela das estações
CREATE TABLE estacoes (
    id_estacao INT PRIMARY KEY AUTO_INCREMENT,
    nome_estacao VARCHAR(100),
    localizacao VARCHAR(100),
    energia_disponivel DECIMAL(5,2),
    tomadas_disponiveis INT
);

-- Tabela de consumo
CREATE TABLE consumo (
    id_consumo INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_estacao INT,
    tempo_uso INT,
    energia_consumida DECIMAL(5,2),
    data_consumo DATE,

    FOREIGN KEY (id_usuario)
    REFERENCES usuarios(id_usuario),

    FOREIGN KEY (id_estacao)
    REFERENCES estacoes(id_estacao)
);