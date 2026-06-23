-- Receita total por Região
SELECT
    regiao,
    SUM(quantidade * preco_unitario) AS receita_total,
    SUM(quantidade * (preco_unitario - custo_unitario)) AS lucro_total
FROM vendas
GROUP BY regiao
ORDER BY receita_total DESC;

-- Margem de lucro por região
SELECT
    regiao,
    SUM(quantidade * preco_unitario) AS receita_total,
    SUM(quantidade * (preco_unitario - custo_unitario)) AS lucro_total,
    ROUND(SUM(quantidade * (preco_unitario - custo_unitario)) /
    SUM(quantidade * preco_unitario) * 100, 2) AS margem_pct
FROM vendas
GROUP BY regiao
ORDER BY margem_pct DESC;

-- Ranking de vendedores por lucro
SELECT
    vendedor,
    COUNT(*) AS total_vendas,
    SUM(quantidade * preco_unitario) AS receita,
    SUM(quantidade * (preco_unitario - custo_unitario)) AS lucro,
    ROUND(SUM(quantidade * (preco_unitario - custo_unitario)) /
    SUM(quantidade * preco_unitario) * 100, 2) AS margem_pct
FROM vendas
GROUP BY vendedor
ORDER BY lucro DESC;

-- Produto mais lucrativo por categoria
SELECT
    categoria,
    produto,
    SUM(quantidade * (preco_unitario - custo_unitario)) AS lucro_total
FROM vendas
GROUP BY categoria, produto
ORDER BY categoria, lucro_total DESC;
