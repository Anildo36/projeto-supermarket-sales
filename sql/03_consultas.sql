-- =========================================
-- 03_consultas.sql
-- Consultas SQL fundamentais sobre a camada raw
-- =========================================

--  total de registros
SELECT COUNT(*) AS total_vendas FROM raw_vendas;

-- Faturamento total por filial 
SELECT branch, SUM(sales::numeric) AS faturamento_total
FROM raw_vendas
GROUP BY branch
ORDER BY faturamento_total DESC;

-- Quantidade de vendas por filial
SELECT branch, COUNT(*) AS qtd_vendas
FROM raw_vendas
GROUP BY branch
ORDER BY qtd_vendas DESC;

-- Faturamento por linha de produto
SELECT product_line, SUM(sales::numeric) AS faturamento_total
FROM raw_vendas
GROUP BY product_line
ORDER BY faturamento_total DESC;

-- Avaliação média por linha de produto
SELECT product_line, AVG(rating::numeric) AS avaliacao_media
FROM raw_vendas
GROUP BY product_line
ORDER BY avaliacao_media DESC;

-- Pagamento mais utilizado
SELECT payment, COUNT(*) AS qtd
FROM raw_vendas
GROUP BY payment
ORDER BY qtd DESC;

-- Valor médio das vendas
SELECT AVG(sales::numeric) AS valor_medio_venda
FROM raw_vendas;

-- Maior venda registrada
SELECT invoice_id, branch, sales
FROM raw_vendas
ORDER BY sales::numeric DESC
LIMIT 1;
