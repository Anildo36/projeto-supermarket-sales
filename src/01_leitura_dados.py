"""
01_leitura_dados.py
Leitura e inspeção inicial do CSV no Pandas.
"""

import pandas as pd

# Caminho do arquivo CSV original
CAMINHO_CSV = "data/raw/SuperMarket Analysis.csv"


def carregar_dados(caminho: str) -> pd.DataFrame:
    """Carrega o CSV original em um DataFrame do Pandas."""
    df = pd.read_csv(caminho)
    return df


def inspecionar_dados(df: pd.DataFrame) -> None:
    """Exibe informações estruturais e estatísticas básicas do DataFrame."""
    print("=" * 60)
    print("PRIMEIRAS LINHAS")
    print("=" * 60)
    print(df.head())

    print("\n" + "=" * 60)
    print("INFORMAÇÕES GERAIS (tipos de dados e valores não nulos)")
    print("=" * 60)
    df.info()

    print("\n" + "=" * 60)
    print("VALORES AUSENTES POR COLUNA")
    print("=" * 60)
    print(df.isnull().sum())

    print("\n" + "=" * 60)
    print("LINHAS DUPLICADAS")
    print("=" * 60)
    print(f"Total de duplicatas: {df.duplicated().sum()}")

    print("\n" + "=" * 60)
    print("ESTATÍSTICAS DESCRITIVAS BÁSICAS")
    print("=" * 60)
    print(df.describe())


if __name__ == "__main__":
    df = carregar_dados(CAMINHO_CSV)
    inspecionar_dados(df)