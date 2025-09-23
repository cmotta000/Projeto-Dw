
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

# CAMINHOS ABSOLUTOS PARA OS CSVs
CAMINHO_CLIENTES = r"C:\Users\tr20890ps\Documents\dw\dados\clientes.csv"
CAMINHO_PRODUTOS = r"C:\Users\tr20890ps\Documents\dw\dados\produtos.csv"
CAMINHO_VENDAS   = r"C:\Users\tr20890ps\Documents\dw\dados\vendas.csv"

# Verificação dos arquivos antes de rodar
for arquivo in [CAMINHO_CLIENTES, CAMINHO_PRODUTOS, CAMINHO_VENDAS]:
    if not os.path.exists(arquivo):
        raise FileNotFoundError(f"⚠️ Arquivo não encontrado: {arquivo}\n"
                                f"Verifique se o caminho está correto!")

# Conexão com o PostgreSQL
try:
    engine = create_engine("postgresql+psycopg2://dsa:dsa1010@localhost:5434/dsadb")
    conn = engine.connect()
    print("✅ Conexão com o banco estabelecida com sucesso!")
except Exception as e:
    raise ConnectionError(f"❌ Não foi possível conectar ao banco de dados.\nErro: {e}")

# Leitura dos CSVs
clientes = pd.read_csv(CAMINHO_CLIENTES)
produtos = pd.read_csv(CAMINHO_PRODUTOS)
vendas   = pd.read_csv(CAMINHO_VENDAS)

# Inserção nas tabelas dimensionais
clientes.to_sql("dim_cliente", engine, schema="dw", if_exists="append", index=False)
produtos.to_sql("dim_produto", engine, schema="dw", if_exists="append", index=False)

# Criar dimensão tempo
dim_tempo = pd.DataFrame()
dim_tempo["data"] = pd.to_datetime(vendas["data"])
dim_tempo["ano"] = dim_tempo["data"].dt.year
dim_tempo["mes"] = dim_tempo["data"].dt.month
dim_tempo["dia"] = dim_tempo["data"].dt.day
dim_tempo["trimestre"] = dim_tempo["data"].dt.quarter
dim_tempo.drop_duplicates(inplace=True)
dim_tempo.to_sql("dim_tempo", engine, schema="dw", if_exists="append", index=False)

# Ler tabelas do banco para recuperar IDs
clientes_db = pd.read_sql("SELECT * FROM dw.dim_cliente", engine)
produtos_db = pd.read_sql("SELECT * FROM dw.dim_produto", engine)
tempo_db    = pd.read_sql("SELECT * FROM dw.dim_tempo", engine)

# Juntar dados e criar tabela fato
vendas = vendas.merge(clientes_db, on="nome")
vendas = vendas.merge(produtos_db, left_on="produto", right_on="nome_produto")
vendas = vendas.merge(tempo_db, on="data")

fato_vendas = vendas[["id_cliente", "id_produto", "id_tempo", "quantidade"]].copy()
fato_vendas["valor_total"] = vendas["quantidade"] * vendas["preco_unitario"]

fato_vendas.to_sql("fato_vendas", engine, schema="dw", if_exists="append", index=False)

print("🎉 Carga de dados concluída com sucesso!")