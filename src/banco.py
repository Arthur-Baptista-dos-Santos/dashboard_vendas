#import duckdb
#import pandas as pd
#
#con = duckdb.connect("dados/vendas.db")
#
#con.execute("CREATE TABLE IF NOT EXISTS vendas AS SELECT * FROM read_csv_auto('dados/vendas.csv')")
#
#resultado = con.execute(open("sql/queries.sql").read()).fetchdf()
#
#print(resultado)
#
#con.close()
#

import duckdb
import pandas as pd

con = duckdb.connect("dados/vendas.db")

con.execute("CREATE OR REPLACE TABLE vendas AS SELECT * FROM read_csv_auto('dados/vendas.csv')")

queries = {
    "Receita por Região": "sql/01_receita_por_regiao.sql",
    "Ranking de Vendedores": "sql/02_ranking_vendedores.sql",
    "Lucro por Categoria": "sql/03_lucro_por_categoria.sql",
}

for titulo, arquivo in queries.items():
    print(f"\n{'='*50}")
    print(f" {titulo}")
    print('='*50)
    resultado = con.execute(open(arquivo).read()).fetchdf()
    print(resultado)

con.close()
