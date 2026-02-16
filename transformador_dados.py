import pandas as pd

def aplicar_regra_credito(df_bruto):
    """Função pura: Recebe um dataframe e retorna um dataframe transformado"""
    df_aprovados = df_bruto[df_bruto['score_credito'] >= 800].copy()
    df_aprovados['status_analise'] = 'Crédito Pré-Aprovado'
    return df_aprovados

def main():
    print("Lendo arquivo bruto...")
    df_bruto = pd.read_parquet("clientes_raw.parquet")
    
    print("Aplicando regras de negócio...")
    df_final = aplicar_regra_credito(df_bruto) # Chamamos a função aqui!
    
    print("Salvando arquivo final...")
    df_final.to_parquet("clientes_aprovados.parquet", index=False)
    print("Concluído!")

if __name__ == "__main__":
    main()
