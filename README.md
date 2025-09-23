🏗️ Projeto Data Warehouse com PostgreSQL + Python (ETL)

Este projeto demonstra como construir um Data Warehouse simples utilizando PostgreSQL (rodando em Docker) e um pipeline ETL em Python.
O objetivo é mostrar, de forma prática, como organizar tabelas dimensão, tabela fato, e realizar a carga de dados para análises.

📋 Estrutura do Projeto
dw/
├── dados/
│   ├── clientes.csv
│   ├── produtos.csv
│   └── vendas.csv
├── pipeline ETL/
│   └── etl.py
└── README.md


dados/ → arquivos de origem simulando base transacional.

pipeline ETL/etl.py → código Python responsável por Extrair, Transformar e Carregar os dados no DW.

PostgreSQL → banco de dados rodando em container Docker, servindo como Data Warehouse.

🚀 Tecnologias Utilizadas

🐳 Docker → para subir o banco de dados PostgreSQL.

🐘 PostgreSQL 16 → armazenamento do Data Warehouse.

🐍 Python 3.9+

pandas → leitura e transformação dos dados.

SQLAlchemy → conexão com o banco.

psycopg2 → driver PostgreSQL.

🏗️ Modelo Dimensional

O projeto utiliza um modelo estrela simples:

dim_clientes → dados dos clientes.

dim_produtos → dados dos produtos.

dim_tempo → datas e atributos de tempo.

fato_vendas → tabela fato que armazena as métricas (quantidade, valor, total).
