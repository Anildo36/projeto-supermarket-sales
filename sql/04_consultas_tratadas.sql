-- ============================================
-- CONSULTAS NA TABELA TRATADA (vendas_tratadas)
-- ============================================

-- Faturamento total por filial
SELECT filial, ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas_tratadas
GROUP BY filial
ORDER BY faturamento DESC;

-- Faturamento por linha de produto
SELECT linha_produto, ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas_tratadas
GROUP BY linha_produto
ORDER BY faturamento DESC;

-- Quantidade de vendas por dia da semana
SELECT dia_semana, COUNT(*) AS qtd_vendas
FROM vendas_tratadas
GROUP BY dia_semana
ORDER BY qtd_vendas DESC;

-- Distribuição por categoria de valor
SELECT categoria_valor, COUNT(*) AS qtd_vendas
FROM vendas_tratadas
GROUP BY categoria_valor
ORDER BY qtd_vendas DESC;