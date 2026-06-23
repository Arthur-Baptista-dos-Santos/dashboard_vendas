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
