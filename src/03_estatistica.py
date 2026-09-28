"""
03_estatistica.py
Estatística descritiva, respostas de negócio e gráficos.
"""

import pandas as pd
import matplotlib.pyplot as plt

CAMINHO_DADOS = "data/processed/vendas_tratadas.csv"
PASTA_GRAFICOS = "resultados/graficos"
PASTA_ESTATISTICAS = "resultados/estatisticas"


def carregar_dados(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)


def responder_perguntas_negocio(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("PERGUNTAS DE NEGÓCIO")
    print("=" * 60)

    # 1. Filial com maior faturamento
    faturamento_filial = df.groupby("filial")["valor_total"].sum().sort_values(ascending=False)
    print(f"\n1. Filial com maior faturamento: {faturamento_filial.index[0]} (${faturamento_filial.iloc[0]:.2f})")

    # 2. Filial com maior quantidade de vendas
    qtd_vendas_filial = df.groupby("filial").size().sort_values(ascending=False)
    print(f"2. Filial com maior quantidade de vendas: {qtd_vendas_filial.index[0]} ({qtd_vendas_filial.iloc[0]} vendas)")

    # 3. Linha de produto com maior faturamento
    faturamento_produto = df.groupby("linha_produto")["valor_total"].sum().sort_values(ascending=False)
    print(f"3. Linha de produto com maior faturamento: {faturamento_produto.index[0]} (${faturamento_produto.iloc[0]:.2f})")

    # 4. Linha de produto com melhor avaliação média
    avaliacao_produto = df.groupby("linha_produto")["avaliacao"].mean().sort_values(ascending=False)
    print(f"4. Linha de produto com melhor avaliação média: {avaliacao_produto.index[0]} ({avaliacao_produto.iloc[0]:.2f})")

    # 5. Forma de pagamento mais utilizada
    pagamento_mais_usado = df["forma_pagamento"].value_counts()
    print(f"5. Forma de pagamento mais utilizada: {pagamento_mais_usado.index[0]} ({pagamento_mais_usado.iloc[0]} vezes)")

    # 6. Valor médio das vendas
    valor_medio = df["valor_total"].mean()
    print(f"6. Valor médio das vendas: ${valor_medio:.2f}")

    # 7. Maior venda registrada
    maior_venda = df.loc[df["valor_total"].idxmax()]
    print(f"7. Maior venda registrada: ${maior_venda['valor_total']:.2f} (Nota {maior_venda['id_venda']}, filial {maior_venda['filial']})")

    # 8. Dia da semana com maior quantidade de vendas
    dia_mais_vendas = df["dia_semana"].value_counts()
    print(f"8. Dia da semana com maior quantidade de vendas: {dia_mais_vendas.index[0]} ({dia_mais_vendas.iloc[0]} vendas)")


def salvar_estatisticas_descritivas(df: pd.DataFrame) -> None:
    resumo = df.describe(include="all")
    resumo.to_csv(f"{PASTA_ESTATISTICAS}/estatisticas_descritivas.csv")
    print(f"\nEstatísticas descritivas salvas em: {PASTA_ESTATISTICAS}/estatisticas_descritivas.csv")


def gerar_graficos(df: pd.DataFrame) -> None:
    # Gráfico 1: Faturamento por filial
    plt.figure(figsize=(8, 5))
    df.groupby("filial")["valor_total"].sum().sort_values().plot(kind="barh", color="steelblue")
    plt.title("Faturamento total por filial")
    plt.xlabel("Faturamento ($)")
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/faturamento_por_filial.png")
    plt.close()

    # Gráfico 2: Faturamento por linha de produto
    plt.figure(figsize=(9, 5))
    df.groupby("linha_produto")["valor_total"].sum().sort_values().plot(kind="barh", color="seagreen")
    plt.title("Faturamento total por linha de produto")
    plt.xlabel("Faturamento ($)")
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/faturamento_por_produto.png")
    plt.close()

    # Gráfico 3: Forma de pagamento mais utilizada
    plt.figure(figsize=(6, 6))
    df["forma_pagamento"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Distribuição das formas de pagamento")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/formas_pagamento.png")
    plt.close()

    # Gráfico 4: Vendas por dia da semana
    plt.figure(figsize=(8, 5))
    ordem_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df["dia_semana"].value_counts().reindex(ordem_dias).plot(kind="bar", color="coral")
    plt.title("Quantidade de vendas por dia da semana")
    plt.ylabel("Quantidade de vendas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/vendas_por_dia_semana.png")
    plt.close()

    print(f"Gráficos salvos em: {PASTA_GRAFICOS}/")


if __name__ == "__main__":
    df = carregar_dados(CAMINHO_DADOS)
    responder_perguntas_negocio(df)
    salvar_estatisticas_descritivas(df)
    gerar_graficos(df)