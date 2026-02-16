# Variáveis para usar o Python do nosso ambiente virtual isolado
PYTHON = .venv/bin/python
PYTEST = .venv/bin/pytest

# O .PHONY diz ao Make que essas palavras são comandos, e não nomes de arquivos
.PHONY: help db-up db-down gerar extrair testar transformar run-all

help:
	@echo "Orquestrador do Pipeline de Dados"
	@echo "Comandos disponíveis:"
	@echo "  make db-up       - Sobe o banco PostgreSQL no Docker"
	@echo "  make gerar       - Insere dados falsos no banco"
	@echo "  make extrair     - Extrai os dados do banco para clientes_raw.parquet"
	@echo "  make testar      - Executa os testes unitários de qualidade (pytest)"
	@echo "  make transformar - Aplica as regras de negócio (gera clientes_aprovados.parquet)"
	@echo "  make run-all     - Executa o fluxo completo"

db-up:
	docker start meu_postgres || echo "O banco já está rodando ou precisa ser recriado."

db-down:
	docker stop meu_postgres

gerar:
	$(PYTHON) gerador_dados.py

extrair:
	$(PYTHON) extrator_parquet.py

testar:
	$(PYTEST) -v test_transformador.py

# A regra transformar tem uma dependência oculta: ela obriga o Make a rodar o 'testar' antes!
transformar: testar
	$(PYTHON) transformador_dados.py

# O pipeline completo dita a ordem exata de execução
run-all: gerar extrair transformar
	@echo "======================================"
	@echo "Pipeline executado com sucesso!"
	@echo "======================================"