import pandas as pd
from transformador_dados import aplicar_regra_credito

def teste_aprovacao_score_limite():
    dados_mock = pd.DataFrame({
        'nome': ['Joao Reprovado', 'Maria no Limite', 'Pedro Aprovado'],
        'score_credito': [799, 800, 850]
    })

    resultado = aplicar_regra_credito(dados_mock)

    assert len(resultado) == 2, "Erro: A quantidade de aprovados está incorreta."

    nomes_aprovados = resultado['nome'].tolist()
    assert 'Joao Reprovado' not in nomes_aprovados, "Erro grave: Cliente com score menor que 800 foi aprovado."

    assert 'status_analise' in resultado.columns, "Erro: A coluna 'status_analise' não foi criada"
    assert resultado.iloc[0]['status_analise'] == 'Crédito Pré-Aprovado', "Erro: O texto do status está incorreto."