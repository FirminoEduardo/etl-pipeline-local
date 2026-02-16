import psycopg2
from faker import Faker
import random

# Inicializa o gerador de dados falsos (em português do Brasil)
fake = Faker('pt_BR')

def conectar_banco():
    """Cria a conexão com o PostgreSQL rodando no Docker"""
    print("Conectando ao banco de dados...")
    conn = psycopg2.connect(
        host="localhost",
        database="dados_db",
        user="engenheiro",
        password="senha_secreta",
        port="5432"
    )
    return conn

def criar_tabela(cursor):
    """Cria a tabela 'clientes' caso ela não exista"""
    print("Criando tabela 'clientes'...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            profissao VARCHAR(100),
            data_nascimento DATE,
            score_credito INTEGER
        );
    """)

def inserir_dados(cursor, quantidade=50):
    """Gera e insere dados falsos na tabela"""
    print(f"Inserindo {quantidade} registros falsos...")
    
    # Query de inserção
    query = "INSERT INTO clientes (nome, profissao, data_nascimento, score_credito) VALUES (%s, %s, %s, %s)"
    
    for _ in range(quantidade):
        nome = fake.name()
        profissao = fake.job()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80)
        score_credito = random.randint(300, 1000)
        
        # Executa a query substituindo os %s pelos dados gerados
        cursor.execute(query, (nome, profissao, data_nascimento, score_credito))

def main():
    # Bloco principal de execução
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        criar_tabela(cursor)
        inserir_dados(cursor, 100) # Inserindo 100 clientes
        
        # Confirma as alterações no banco (commit)
        conn.commit()
        print("Sucesso! Dados inseridos com sucesso.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        conn.rollback() # Desfaz as alterações em caso de erro
        
    finally:
        # Sempre feche a conexão no final
        cursor.close()
        conn.close()
        print("Conexão encerrada.")

if __name__ == "__main__":
    main()
