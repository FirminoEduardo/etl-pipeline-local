# 🚀 ETL Pipeline Local com Qualidade de Dados (Data Quality)

Este projeto é um pipeline de Engenharia de Dados construído do zero para simular um fluxo real de ponta a ponta (Extração, Transformação e Carga), focando fortemente em **boas práticas de engenharia de software**, testes automatizados e orquestração.

## 🏗️ Arquitetura do Projeto

O pipeline simula a ingestão de dados de um sistema transacional, convertendo os dados para um formato analítico colunar (Parquet) e aplicando regras de negócios rigorosas validadas por testes unitários.

1. **Origem (Banco de Dados):** Container Docker rodando PostgreSQL.
2. **Geração de Dados:** Script Python injeta dados fictícios de clientes e scores de crédito.
3. **Extração (Extract):** Leitura otimizada via SQLAlchemy e Pandas.
4. **Validação (Data Quality):** Bateria de testes com `pytest` para garantir que a regra de negócio não quebre.
5. **Transformação (Transform):** Filtro analítico isolando clientes com Score >= 800.
6. **Destino (Load):** Salvamento local particionado em formato `.parquet` usando `pyarrow`.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11 (Isolado via `pyenv` / `venv`)
* **Banco de Dados:** PostgreSQL (via Docker)
* **Processamento de Dados:** Pandas, Pyarrow
* **Testes e Qualidade:** Pytest
* **Orquestração:** GNU Make (Makefile)

## ⚙️ Pré-requisitos

Para rodar este projeto na sua máquina, você precisará de:
* Linux/macOS com `make` instalado.
* Docker instalado e rodando.
* Python 3.11+ e `pip`.

## 🚀 Como Executar

Este projeto utiliza um `Makefile` para orquestrar todos os scripts, facilitando a execução sem precisar lembrar a ordem de cada comando.

1. **Clone o repositório e instale as dependências:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install pandas pyarrow sqlalchemy psycopg2-binary faker pytest

2. **Suba o banco de dados via Docker:**
    ```bash
    make db-up
   ``` 
    Execute o pipeline completo (Geração -> Extração -> Testes -> Transformação):
    ```bash
    make run-all
   ```
3. **Comandos Individuais (Orquestrador)**

Se preferir rodar passo a passo, você pode utilizar:

    make gerar: Injeta dados sintéticos no Postgres.

    make extrair: Extrai para clientes_raw.parquet.

    make testar: Roda a validação de qualidade de dados (pytest).

    make transformar: Aplica regras de negócio e gera clientes_aprovados.parquet.
