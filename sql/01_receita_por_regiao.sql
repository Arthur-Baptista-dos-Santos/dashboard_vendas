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
