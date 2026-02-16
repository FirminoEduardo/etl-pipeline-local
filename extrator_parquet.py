import pandas as pd
from sqlalchemy import create_engine

def main():
    print("Iniciando extração de dados... ")

    db_uri = "postgresql+psycopg2://engenheiro:senha_secreta@localhost:5432/dados_db"

    engine = create_engine(db_uri)

    query = "SELECT * FROM clientes;"

    try:

        print("Lendo dados do Postgresql para memória")
        df = pd.read_sql(query, engine)

        print("/n Pré-visualização dos dados extraídos")
        print(df.head())

        arquivo_destino = "clientes_raw.parquet"
        print(f"/nArquivos salvos em: {arquivo_destino}")

        df.to_parquet(arquivo_destino, engine='pyarrow', index=False)

        print("/n Sucesso!")
    except Exception as e:
        print("Erro durante a extração {e}")

if __name__ == "__main__":
    main()