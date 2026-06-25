import duckdb
import matplotlib.pyplot as plt


def carregar_dados(caminho_db: str = "dados/vendas.db") -> tuple:
    con = duckdb.connect(caminho_db)
    regiao = con.execute(open("sql/01_receita_por_regiao.sql").read()).fetchdf()
    vendedores = con.execute(open("sql/02_ranking_vendedores.sql").read()).fetchdf()
    categorias = con.execute(open("sql/03_lucro_por_categoria.sql").read()).fetchdf()
    con.close()
    return regiao, vendedores, categorias


def gerar_dashboard(caminho_db: str = "dados/vendas.db") -> None:
    regiao, vendedores, categorias = carregar_dados(caminho_db)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    axes[0].barh(regiao["regiao"], regiao["receita_total"], color="steelblue")
    axes[0].set_title("Receita por Região")
    axes[0].set_xlabel("R$")

    axes[1].bar(vendedores["vendedor"], vendedores["margem_pct"], color="seagreen")
    axes[1].set_title("Margem % por Vendedor")
    axes[1].set_ylabel("%")
    axes[1].axhline(vendedores["margem_pct"].mean(), color="red", linestyle="--", label="Média")
    axes[1].legend()

    axes[2].barh(categorias["produto"], categorias["lucro_total"], color="coral")
    axes[2].set_title("Lucro por Produto")
    axes[2].set_xlabel("R$")

    plt.tight_layout()
    plt.savefig("dados/dashboard.png")
    plt.show()
    print("Dashboard salvo em dados/dashboard.png")


def main() -> None:
    gerar_dashboard()


if __name__ == "__main__":
    main()
