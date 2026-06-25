import duckdb


def inicializar(caminho_db: str = "dados/vendas.db", caminho_csv: str = "dados/vendas.csv") -> None:
    con = duckdb.connect(caminho_db)
    con.execute(f"CREATE OR REPLACE TABLE vendas AS SELECT * FROM read_csv_auto('{caminho_csv}')")
    con.close()
    print("Banco inicializado em", caminho_db)


def executar_queries(caminho_db: str = "dados/vendas.db") -> None:
    queries = {
        "Receita por Região": "sql/01_receita_por_regiao.sql",
        "Ranking de Vendedores": "sql/02_ranking_vendedores.sql",
        "Lucro por Produto": "sql/03_lucro_por_categoria.sql",
    }
    con = duckdb.connect(caminho_db)
    for titulo, arquivo in queries.items():
        print(f"\n{'='*50}\n {titulo}\n{'='*50}")
        print(con.execute(open(arquivo).read()).fetchdf())
    con.close()


def main() -> None:
    inicializar()
    executar_queries()


if __name__ == "__main__":
    main()
