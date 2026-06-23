-- Produto mais lucrativo por categoria
SELECT
    categoria,
    produto,
    SUM(quantidade * (preco_unitario - custo_unitario)) AS lucro_total
FROM vendas
GROUP BY categoria, produto
ORDER BY categoria, lucro_total DESC;
