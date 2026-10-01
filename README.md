# Projeto Supermarket Sales — Pipeline de Análise de Dados

Projeto avaliativo do Módulo 1 do curso de Análise de Dados com Python. Constrói um pipeline completo de dados, desde a ingestão bruta no PostgreSQL até a geração de insights de negócio com Python e Pandas, inspirado na Arquitetura Medallion (Raw → Tratada → Gold).

## 📋 Sobre o projeto

Uma rede de supermercados registra suas vendas diariamente. Este projeto organiza esses dados brutos, trata e analisa as informações para responder perguntas fundamentais de negócio, como faturamento por filial, produto mais vendido e forma de pagamento mais utilizada.

**Fonte dos dados:** [Supermarket Sales — Kaggle](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

## 🛠️ Tecnologias utilizadas

- **PostgreSQL** — armazenamento das camadas Raw e Tratada
- **DBeaver** — cliente para administração do banco e importação dos dados
- **SQL** — consultas e exportação de dados
- **Python 3** — linguagem principal do tratamento e análise
- **Pandas** — limpeza, tipagem e transformação dos dados
- **Matplotlib** — geração de gráficos
- **python-dotenv** — gerenciamento seguro de credenciais
- **Git / GitHub Desktop** — controle de versão

## 📁 Estrutura do projeto

projeto-supermarket-sales/
├── sql/
│ ├── 01_criar_banco.sql # Criação do banco de dados
│ ├── 02_criar_tabelas.sql # Criação das tabelas Raw e Tratada
│ ├── 03_consultas.sql # Consultas SQL sobre a camada Raw
│ └── 04_consultas_tratadas.sql # Consultas SQL sobre a camada Tratada
├── src/
│ ├── 01_leitura_dados.py # Leitura e inspeção inicial do CSV
│ ├── 02_etl_vendas.py # Limpeza, tipagem e colunas derivadas
│ ├── 03_estatistica.py # Estatística descritiva e gráficos
│ └── 04_carga_tratada.py # Carrega os dados tratados de volta no PostgreSQL
├── data/
│ ├── raw/ # Dados originais (CSV do Kaggle)
│ └── processed/ # Dados tratados (vendas_tratadas.csv)
├── resultados/
│ ├── estatisticas/ # Estatísticas descritivas (CSV)
│ └── graficos/ # Gráficos gerados (PNG)
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos ignorados pelo Git
└── README.md


## ⚙️ Como executar o projeto

### Pré-requisitos
- PostgreSQL instalado e rodando
- Python 3.10+ instalado
- DBeaver (ou outro cliente SQL de sua preferência)

### 1. Clonar o repositório
```bash
git clone https://github.com/Anildo36/projeto-supermarket-sales.git
cd projeto-supermarket-sales
```

### 2. Criar o banco de dados
Execute o script `sql/01_criar_banco.sql` no seu servidor PostgreSQL (via DBeaver ou psql).

### 3. Criar as tabelas
Execute o script `sql/02_criar_tabelas.sql` no banco `supermarket_sales` criado no passo anterior. Isso cria as tabelas `raw_vendas` (camada Raw) e `vendas_tratadas` (camada Tratada).

### 4. Carregar os dados brutos
Baixe o CSV do [dataset no Kaggle](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales), salve em `data/raw/`, e importe o conteúdo para a tabela `raw_vendas` (pode ser feito pela ferramenta de importação do DBeaver).

### 5. Rodar as consultas SQL sobre a camada Raw
Execute `sql/03_consultas.sql` para explorar os dados brutos diretamente no banco e exportar um CSV de apoio.

### 6. Configurar o ambiente Python
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

### 7. Criar o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto (não versionado, protegido pelo `.gitignore`) com suas credenciais do PostgreSQL:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=supermarket_sales
DB_USER=postgres
DB_PASSWORD=sua_senha
```

### 8. Executar o pipeline Python, em ordem
```bash
python src/01_leitura_dados.py
python src/02_etl_vendas.py
python src/03_estatistica.py
```

### 9. Carregar os dados tratados de volta no PostgreSQL
```bash
python src/04_carga_tratada.py
```
Esse script carrega o arquivo `data/processed/vendas_tratadas.csv` para a tabela `vendas_tratadas` no PostgreSQL.

### 10. Rodar as consultas SQL sobre a camada Tratada
Execute `sql/04_consultas_tratadas.sql` para explorar os dados já tratados diretamente no banco (faturamento por filial, por produto, vendas por dia da semana e por categoria de valor).

## 📊 Resultados obtidos

Com base na análise de 1000 registros de vendas:

| Pergunta de negócio | Resposta |
|---|---|
| Filial com maior faturamento | **Giza** ($110.568,71) |
| Filial com maior quantidade de vendas | **Alex** (340 vendas) |
| Linha de produto com maior faturamento | **Food and beverages** ($56.144,84) |
| Linha de produto com melhor avaliação média | **Food and beverages** (7,11) |
| Forma de pagamento mais utilizada | **Ewallet** (345 vezes) |
| Valor médio das vendas | **$322,97** |
| Maior venda registrada | **$1.042,65** (filial Giza) |
| Dia da semana com maior quantidade de vendas | **Sábado** (164 vendas) |

Os gráficos completos estão disponíveis em `resultados/graficos/`:
- `faturamento_por_filial.png`
- `faturamento_por_produto.png`
- `formas_pagamento.png`
- `vendas_por_dia_semana.png`

E as estatísticas descritivas completas em `resultados/estatisticas/estatisticas_descritivas.csv`.

## 💡 Possíveis melhorias futuras

- Automatizar a carga do CSV bruto para o PostgreSQL via script Python (em vez da importação manual pelo DBeaver)
- Adicionar testes automatizados para as funções de tratamento de dados
- Criar um dashboard interativo (Streamlit ou Power BI) para explorar os resultados
- Adicionar análise de série temporal para identificar sazonalidade nas vendas

## 👤 Autor

**Anildo Dos Santos**
Projeto desenvolvido como atividade avaliativa do curso de Análise de Dados com Python — Módulo 1.

- GitHub: [@Anildo36](https://github.com/Anildo36)