-- ====================================
-- 02_criar_tabelas.sql
-- Criação das tabelas Raw e Tratada
-- ======================================

-- ============================================
-- CAMADA RAW
--  CSV copiado do original, sem alterações
-- ====================================
CREATE TABLE raw_vendas (
    invoice_id                 VARCHAR(50) PRIMARY KEY,
    branch                     VARCHAR(10),
    city                       VARCHAR(100),
    customer_type              VARCHAR(50),
    gender                     VARCHAR(20),
    product_line               VARCHAR(150),
    unit_price                 VARCHAR(20),   -- foi mantido como texto na Raw (copia sendo fiel a original)
    quantity                   VARCHAR(20),
    tax_5_percent               VARCHAR(20),
    sales                      VARCHAR(20),
    date                       VARCHAR(20),
    time                       VARCHAR(20),
    payment                    VARCHAR(50),
    cogs                       VARCHAR(20),
    gross_margin_percentage    VARCHAR(30),
    gross_income               VARCHAR(20),
    rating                     VARCHAR(10)
);

-- ============================================
-- CAMADA TODA COM OS RESULTADOS TRATADOS
-- Dados tipados e com colunas conforme
-- o dicionário da camada silver
-- ============================================
CREATE TABLE vendas_tratada (
    id_venda            VARCHAR(50) PRIMARY KEY NOT NULL,
    filial               VARCHAR(10) NOT NULL,
    cidade               VARCHAR(100) NOT NULL,
    tipo_cliente         VARCHAR(50),
    genero               VARCHAR(20),
    linha_produto        VARCHAR(150) NOT NULL,
    preco_unitario       NUMERIC(10,2) CHECK (preco_unitario >= 0),
    quantidade           INTEGER CHECK (quantidade > 0),
    imposto              NUMERIC(10,2) CHECK (imposto >= 0),
    valor_total          NUMERIC(12,2) CHECK (valor_total >= 0),
    data_venda           DATE,
    hora_venda           TIME,
    forma_pagamento      VARCHAR(50) NOT NULL,
    custo_mercadoria     NUMERIC(12,2) CHECK (custo_mercadoria >= 0),
    margem_percentual    NUMERIC(10,2),
    receita_bruta        NUMERIC(12,2) CHECK (receita_bruta >= 0),
    avaliacao            NUMERIC(4,2) CHECK (avaliacao BETWEEN 0 AND 10)
);