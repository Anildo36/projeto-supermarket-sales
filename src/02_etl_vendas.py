"""
02_etl_vendas.py
Limpeza, tipagem, tratamento de nulos e colunas derivadas.
Gera o arquivo tratado em data/processed/vendas_tratadas.csv
"""

import pandas as pd

CAMINHO_ENTRADA = "data/raw/SuperMarket Analysis.csv"
CAMINHO_SAIDA = "data/processed/vendas_tratadas.csv"


def carregar_dados(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)


def renomear_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """Renomeia colunas para o padrão do dicionário de dados (sem espaços/acentos)."""
    df = df.rename(columns={
        "Invoice ID": "id_venda",
        "Branch": "filial",
        "City": "cidade",
        "Customer type": "tipo_cliente",
        "Gender": "genero",
        "Product line": "linha_produto",
        "Unit price": "preco_unitario",
        "Quantity": "quantidade",
        "Tax 5%": "imposto",
        "Sales": "valor_total",
        "Date": "data_venda",
        "Time": "hora_venda",
        "Payment": "forma_pagamento",
        "cogs": "custo_mercadoria",
        "gross margin percentage": "margem_percentual",
        "gross income": "receita_bruta",
        "Rating": "avaliacao",
    })
    return df


def tratar_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Converte tipos de dados (datas, remove duplicidades)."""
    df["data_venda"] = pd.to_datetime(df["data_venda"], format="%m/%d/%Y").dt.date
    df["hora_venda"] = pd.to_datetime(df["hora_venda"], format="%I:%M:%S %p").dt.time
    df = df.drop_duplicates()
    return df


def criar_colunas_derivadas(df: pd.DataFrame) -> pd.DataFrame:
    """Cria colunas derivadas para apoiar a análise de negócio."""
    df["dia_semana"] = pd.to_datetime(df["data_venda"]).dt.day_name()
    df["mes"] = pd.to_datetime(df["data_venda"]).dt.month
    df["categoria_valor"] = pd.cut(
        df["valor_total"],
        bins=[0, 200, 500, float("inf")],
        labels=["Baixo", "Médio", "Alto"],
    )
    return df


def validar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica validações básicas (equivalente às CHECK constraints do banco)."""
    df = df[df["preco_unitario"] >= 0]
    df = df[df["quantidade"] > 0]
    df = df[df["valor_total"] >= 0]
    df = df[(df["avaliacao"] >= 0) & (df["avaliacao"] <= 10)]
    return df


if __name__ == "__main__":
    df = carregar_dados(CAMINHO_ENTRADA)
    df = renomear_colunas(df)
    df = tratar_tipos(df)
    df = criar_colunas_derivadas(df)
    df = validar_dados(df)

    df.to_csv(CAMINHO_SAIDA, index=False)

    print(f"Dados tratados salvos em: {CAMINHO_SAIDA}")
    print(f"Total de linhas após tratamento: {len(df)}")
    print("\nColunas finais:")
    print(df.columns.tolist())