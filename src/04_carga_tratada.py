"""
04_carga_tratada.py
Carrega o CSV tratado (data/processed/vendas_tratadas.csv)
na tabela vendas_tratadas do PostgreSQL.
"""

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

CAMINHO_CSV = "data/processed/vendas_tratadas.csv"
TABELA = "vendas_tratadas"


def criar_conexao():
    """Cria a conexão com o PostgreSQL usando as variáveis do .env."""
    load_dotenv()
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")
    url = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
    return create_engine(url)


def carregar_csv(caminho: str) -> pd.DataFrame:
    """Lê o CSV tratado e converte data e hora para os tipos do banco."""
    df = pd.read_csv(caminho)
    df["data_venda"] = pd.to_datetime(df["data_venda"]).dt.date
    df["hora_venda"] = pd.to_datetime(df["hora_venda"], format="%H:%M:%S").dt.time
    return df


def carregar_no_banco(df: pd.DataFrame, engine) -> None:
    """Limpa a tabela (evita duplicar ao rodar de novo) e insere os dados."""
    with engine.begin() as conexao:
        conexao.execute(text(f"TRUNCATE TABLE {TABELA}"))
    df.to_sql(TABELA, engine, if_exists="append", index=False)


if __name__ == "__main__":
    engine = criar_conexao()
    df = carregar_csv(CAMINHO_CSV)
    carregar_no_banco(df, engine)
    print(f"{len(df)} linhas carregadas em {TABELA}")